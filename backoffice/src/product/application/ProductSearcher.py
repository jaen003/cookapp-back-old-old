"""
 *
 * Libraries 
 *
"""

from src.product.domain import ProductRepository
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
    ) -> list:
        # Variables
        repository : ProductRepository
        products   : list
        # Code
        repository = self.__repository
        products   = repository.selectAllByNameAndRestaurant( name, restaurantId )
        return products
    
    def searchAllByRestaurant( 
        self,
        restaurantId : RestaurantId,
    ) -> list:
        # Variables
        repository : ProductRepository
        products   : list
        # Code
        repository = self.__repository
        products   = repository.selectAllByRestaurant( restaurantId )
        return products
