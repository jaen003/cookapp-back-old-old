"""
 *
 * Libraries 
 *
"""

from src.user.domain       import UserName
from src.user.domain       import UserPassword
from src.shared.domain     import UserEmail
from src.shared.domain     import RestaurantId
from src.user.domain       import UserRepository
from src.user.domain       import Administrator
from src.user.domain       import Chef
from src.user.domain       import Waiter
from src.shared.domain     import SUCCESSFUL_REQUEST
from src.shared.domain     import SERVER_INTERNAL_ERROR
from src.shared.domain     import DomainException
from src.user.domain       import UserFinder
from src.shared.domain     import USER_ALREADY_CREATED
from src.shared.domain     import EventBus
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder
from src.user.domain       import User

"""
 *
 * Classes 
 *
"""

class UserInsurer:

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

    def insure( 
        self, 
        email        : UserEmail,
        password     : UserPassword,
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
            user.insure( password )
            if repository.update( user ):
                eventBus.publish( user.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()