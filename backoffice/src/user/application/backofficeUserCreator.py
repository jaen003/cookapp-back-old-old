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
from src.shared.domain     import UuidValueObject

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
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventBus             = eventBus

    def createAdministrator( 
        self, 
        email    : UserEmail, 
        name     : UserName,
        password : UserPassword,
    ) -> int:
        # Variables
        user                : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurant           : Restaurant
        restaurantId         : RestaurantId
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        try:
            restaurant   = Restaurant.create( UuidValueObject.random() )
            restaurantId = restaurant.id()
            user = Administrator.create( email, name, password, restaurantId )
            try:            
                finder.findByEmail( email )
                return USER_ALREADY_CREATED
            except DomainException:
                pass
            if not restaurantRepository.insert( restaurant ):
                return SERVER_INTERNAL_ERROR
            if not repository.insert( user ):
                return SERVER_INTERNAL_ERROR
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
            user = Chef.create( email, name, UserPassword.short(), restaurantId )
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
            user = Waiter.create( email, name, UserPassword.short(), restaurantId )
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