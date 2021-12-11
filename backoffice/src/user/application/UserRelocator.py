"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRole
from src.shared.domain import UserEmail
from src.user.domain   import UserRepository
from src.user.domain   import User
from src.user.domain   import UserFinder
from src.shared.domain import EventBus
from src.shared.domain import RestaurantId
from src.shared.domain import ServerInternalErrorException
from src.user.domain   import UserNotFoundException

"""
 *
 * Classes 
 *
"""

class UserRelocator:

    """
     *
     * Parameters 
     *
    """
 
    __repository : UserRepository
    __eventBus   : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository : UserRepository,
        eventBus   : EventBus,
    ) -> None:
        self.__repository = repository
        self.__eventBus   = eventBus

    def relocate( 
        self, 
        email        : UserEmail, 
        role         : UserRole,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        user       : User
        repository : UserRepository
        finder     : UserFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = UserFinder( repository )
        user       = finder.findByEmailAndRestaurant( email, restaurantId )
        if user is None:
            raise UserNotFoundException( email )
        user.relocate( role )
        if not repository.update( user ):
            raise ServerInternalErrorException()
        eventBus.publish( user.pullEvents() )
