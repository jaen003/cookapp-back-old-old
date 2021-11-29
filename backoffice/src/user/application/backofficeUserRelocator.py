"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRole
from src.shared.domain import UserEmail
from src.user.domain   import UserRepository
from src.user.domain   import User
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import SERVER_INTERNAL_ERROR
from src.shared.domain import DomainException
from src.user.domain   import UserFinder
from src.shared.domain import EventBus
from src.shared.domain import RestaurantId

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
    ) -> int:
        # Variables
        user       : User
        repository : UserRepository
        finder     : UserFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = UserFinder( repository )
        try:
            user = finder.findByEmailAndRestaurant( email, restaurantId )
            user.relocate( role )
            if repository.update( user ):
                eventBus.publish( user.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
