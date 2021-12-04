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
from src.restaurant.domain import Restaurant
from src.user.domain       import UserCode

"""
 *
 * Classes 
 *
"""

class UserCreator:

    """
     *
     * Parameters 
     *
    """
 
    __repository           : UserRepository
    __volatileRepository   : UserRepository
    __restaurantRepository : RestaurantRepository
    __eventBus             : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : UserRepository,
        restaurantRepository : RestaurantRepository,
        eventBus             : EventBus,
        volatileRepository   : UserRepository = None,
    ) -> None:
        self.__repository           = repository
        self.__volatileRepository   = volatileRepository
        self.__restaurantRepository = restaurantRepository
        self.__eventBus             = eventBus

    def createAdministrator( 
        self, 
        email    : UserEmail, 
        name     : UserName,
        password : UserPassword,
    ) -> int:
        # Variables
        user                 : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        volatileRepository   : UserRepository
        restaurant           : Restaurant
        restaurantId         : RestaurantId
        code                 : UserCode
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        volatileRepository   = self.__volatileRepository
        try:
            restaurant   = Restaurant.create()
            restaurantId = restaurant.id()
            code         = UserCode.short()
            user = Administrator.create( email, name, password, restaurantId, code )
            try:            
                finder.findByEmail( email )
                return USER_ALREADY_CREATED
            except DomainException:
                pass
            if not restaurantRepository.insert( restaurant ):
                return SERVER_INTERNAL_ERROR
            if not repository.insert( user ):
                return SERVER_INTERNAL_ERROR
            volatileRepository.insert( user )
            eventBus.publish( user.pullEvents() )
            return SUCCESSFUL_REQUEST
        except DomainException as exc:
            return exc.code()
    
    def createChef( 
        self,
        email        : UserEmail, 
        name         : UserName,
        restaurantId : RestaurantId,
    ) -> int:
        # Variables
        user                 : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        try:
            user = Chef.create( email, name, UserPassword.weak(), restaurantId )
            restaurantFinder.findById( restaurantId )
            try:            
                finder.findByEmailAndRestaurant( email, restaurantId )
                return USER_ALREADY_CREATED
            except DomainException:
                pass
            if repository.insert( user ):
                eventBus.publish( user.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
    
    def createWaiter( 
        self, 
        email        : UserEmail, 
        name         : UserName,
        restaurantId : RestaurantId,
    ) -> int:
        # Variables
        user                : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        try:
            user = Waiter.create( email, name, UserPassword.weak(), restaurantId )
            restaurantFinder.findById( restaurantId )
            try:            
                finder.findByEmailAndRestaurant( email, restaurantId )
                return USER_ALREADY_CREATED
            except DomainException:
                pass
            if repository.insert( user ):
                eventBus.publish( user.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()