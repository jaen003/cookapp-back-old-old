"""
 *
 * Libraries 
 *
"""

from src.product.domain import ProductRepository
from src.shared.domain  import SUCCESSFUL_REQUEST
from src.shared.domain  import DomainException
from src.product.domain import ProductName
from src.shared.domain  import RestaurantId

"""
 *
 * Classes 
 *
"""

class ProductSearcher:

    """
     *
     * Parameters 
     *
    """
 
    __repository : ProductRepository

    """
     *
     * Methods 
     *
    """

    def __init__( self, repository : ProductRepository ) -> None:
        self.__repository = repository

    def searchAllByNameAndRestaurant( 
        self,
        name         : ProductName,
        restaurantId : RestaurantId,
    ) -> tuple[ list, int ]:
        # Variables
        repository : ProductRepository
        products   : list
        # Code
        repository = self.__repository
        products   = repository.selectAllByNameAndRestaurant( name, restaurantId )
        return products, SUCCESSFUL_REQUEST
    
    def searchAllByRestaurant( 
        self,
        restaurantId : RestaurantId,
    ) -> tuple[ list, int ]:
        # Variables
        repository : ProductRepository
        products   : list
        # Code
        repository = self.__repository
        products   = repository.selectAllByRestaurant( restaurantId )
        return products, SUCCESSFUL_REQUEST
