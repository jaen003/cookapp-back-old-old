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
from src.user.domain       import UserFinder
from src.shared.domain     import EventBus
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder
from src.user.domain       import User
from src.restaurant.domain import Restaurant
from src.shared.domain     import ServerInternalErrorException
from src.restaurant.domain import RestaurantNotFoundException
from src.user.domain       import UserAlreadyCreatedException

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
    ) -> None:
        # Variables
        user                 : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        volatileRepository   : UserRepository
        restaurant           : Restaurant
        restaurantId         : RestaurantId
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        volatileRepository   = self.__volatileRepository
        user                 = finder.findByEmail( email )
        if user is not None:
            raise UserAlreadyCreatedException( email )
        restaurant   = Restaurant.create()
        restaurantId = restaurant.id()
        user = Administrator.create( email, name, password, restaurantId )
        if not restaurantRepository.insert( restaurant ):
            raise ServerInternalErrorException()
        if not repository.insert( user ):
            raise ServerInternalErrorException()
        volatileRepository.insert( user )
        eventBus.publish( user.pullEvents() )
    
    def createChef( 
        self,
        email        : UserEmail, 
        name         : UserName,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        user                 : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        restaurant           : Restaurant
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        restaurant           = restaurantFinder.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        user = finder.findByEmailAndRestaurant( email, restaurantId )
        if user is not None:
            raise UserAlreadyCreatedException( email )
        user = Chef.create( email, name, UserPassword.weak(), restaurantId )
        if not repository.insert( user ):
            raise ServerInternalErrorException()
        eventBus.publish( user.pullEvents() )
    
    def createWaiter( 
        self, 
        email        : UserEmail, 
        name         : UserName,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        user                : User
        repository           : UserRepository
        finder               : UserFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        restaurant           : Restaurant
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = UserFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        restaurant           = restaurantFinder.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        user = finder.findByEmailAndRestaurant( email, restaurantId )
        if user is not None:
            raise UserAlreadyCreatedException( email )
        user = Waiter.create( email, name, UserPassword.weak(), restaurantId )
        if not repository.insert( user ):
            raise ServerInternalErrorException()
        eventBus.publish( user.pullEvents() )