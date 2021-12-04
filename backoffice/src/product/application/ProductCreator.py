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
from src.shared.domain     import SUCCESSFUL_REQUEST
from src.shared.domain     import SERVER_INTERNAL_ERROR
from src.shared.domain     import DomainException
from src.product.domain    import ProductFinder
from src.shared.domain     import PRODUCT_ALREADY_CREATED
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder
from src.shared.domain     import EventBus
from src.shared.domain     import RestaurantId

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
    ) -> int:
        # Variables
        product              : Product
        repository           : ProductRepository
        restaurantRepository : RestaurantRepository
        finder               : ProductFinder
        restaurantFinder     : RestaurantFinder
        eventBus             : EventBus
        # Code
        eventBus             = self.__eventBus
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        repository           = self.__repository
        finder               = ProductFinder( repository )
        try:
            product = Product.create( id, name, price, description, restaurantId )
            restaurantFinder.findById( restaurantId )
            try:            
                finder.findByNameAndRestaurant( name, restaurantId )
                return PRODUCT_ALREADY_CREATED
            except DomainException:
                pass
            if repository.insert( product ):
                eventBus.publish( product.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
