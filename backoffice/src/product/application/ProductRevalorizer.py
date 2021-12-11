"""
 *
 * Libraries 
 *
"""

from src.product.domain import ProductNotFoundException
from src.shared.domain  import ServerInternalErrorException
from src.product.domain import ProductPrice
from src.shared.domain  import ProductId
from src.product.domain import ProductRepository
from src.product.domain import Product
from src.product.domain import ProductFinder
from src.shared.domain  import EventBus
from src.shared.domain  import RestaurantId

"""
 *
 * Classes 
 *
"""

class ProductRevalorizer:

    """
     *
     * Parameters 
     *
    """
 
    __repository : ProductRepository
    __eventBus   : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository : ProductRepository,
        eventBus   : EventBus,
    ) -> None:
        self.__repository = repository
        self.__eventBus   = eventBus

    def revalue(
        self, 
        id           : ProductId,
        price        : ProductPrice,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        product    : Product
        repository : ProductRepository
        finder     : ProductFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = ProductFinder( repository )
        product    = finder.findByIdAndRestaurant( id, restaurantId )
        if product is None:
            raise ProductNotFoundException( id )
        product.revalue( price )
        if not repository.update( product ):
            raise ServerInternalErrorException()
        eventBus.publish( product.pullEvents() )