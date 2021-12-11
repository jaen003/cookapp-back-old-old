"""
 *
 * Libraries 
 *
"""

from src.product.domain    import ProductName
from src.product.domain    import ProductPrice
from src.product.domain    import ProductDescription
from src.shared.domain     import ProductId
from src.product.domain    import ProductRepository
from src.product.domain    import Product
from src.product.domain    import ProductFinder
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder
from src.shared.domain     import EventBus
from src.shared.domain     import RestaurantId
from src.restaurant.domain import RestaurantNotFoundException
from src.shared.domain     import ServerInternalErrorException
from src.product.domain    import ProductNameAlreadyCreatedException
from src.restaurant.domain import Restaurant

"""
 *
 * Classes 
 *
"""

class ProductCreator:

    """
     *
     * Parameters 
     *
    """
 
    __repository           : ProductRepository
    __restaurantRepository : RestaurantRepository
    __eventBus             : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : ProductRepository,
        restaurantRepository : RestaurantRepository,
        eventBus             : EventBus,
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventBus             = eventBus

    def create( 
        self, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        product              : Product
        repository           : ProductRepository
        restaurantRepository : RestaurantRepository
        finder               : ProductFinder
        restaurantFinder     : RestaurantFinder
        eventBus             : EventBus
        restaurant           : Restaurant
        # Code
        eventBus             = self.__eventBus
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        repository           = self.__repository
        finder               = ProductFinder( repository )
        restaurant           = restaurantFinder.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        product = finder.findByNameAndRestaurant( name, restaurantId )
        if product is not None:
            raise ProductNameAlreadyCreatedException( name )
        product = Product.create( id, name, price, description, restaurantId )     
        if not repository.insert( product ):
            raise ServerInternalErrorException()
        eventBus.publish( product.pullEvents() )
