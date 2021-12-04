"""
 *
 * Libraries 
 *
"""

from src.product.domain import ProductDescription
from src.shared.domain  import ProductId
from src.product.domain import ProductRepository
from src.product.domain import Product
from src.shared.domain  import SUCCESSFUL_REQUEST
from src.shared.domain  import SERVER_INTERNAL_ERROR
from src.shared.domain  import DomainException
from src.product.domain import ProductFinder
from src.shared.domain  import EventBus
from src.shared.domain  import RestaurantId

"""
 *
 * Classes 
 *
"""

class ProductRewriter:

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

    def rewrite( 
        self, 
        id           : ProductId, 
        description  : ProductDescription,
        restaurantId : RestaurantId,
    ) -> int:
        # Variables
        product    : Product
        repository : ProductRepository
        finder     : ProductFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = ProductFinder( repository )
        try:
            product = finder.findByIdAndRestaurant( id, restaurantId )
            product.rewrite( description )
            if repository.update( product ):
                eventBus.publish( product.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
