"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRepository
from src.user.domain   import UserFinder
from src.user.domain   import User
from src.shared.domain import UserEmail
from src.shared.domain import RestaurantId
from src.shared.domain import EventBus
from src.shared.domain import ServerInternalErrorException
from src.user.domain   import UserNotFoundException

"""
 *
 * Classes 
 *
"""

class UserDeletor:

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
    
    def delete( 
        self,
        email        : UserEmail,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        repository : UserRepository
        finder     : UserFinder
        user       : User
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = UserFinder( repository )
        user       = finder.findByEmailAndRestaurant( email, restaurantId )
        if user is None:
            raise UserNotFoundException( email )
        user.delete()
        if not repository.update( user ):
            raise ServerInternalErrorException()
        eventBus.publish( user.pullEvents() )
