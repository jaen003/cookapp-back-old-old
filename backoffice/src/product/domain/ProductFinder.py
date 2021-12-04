"""
 *
 * Libraries 
 *
"""

from .ProductNotFoundException     import ProductNotFoundException
from .ProductRepository            import ProductRepository
from src.shared.domain             import ProductId
from src.shared.domain             import RestaurantId
from .Product                      import Product 
from src.product.domain            import ProductName
from .ProductNameNotFoundException import ProductNameNotFoundException

"""
 *
 * Classes
 *
"""

class ProductFinder:

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
    
    def findByIdAndRestaurant( self, id : ProductId, restaurantId : RestaurantId ) -> Product:
        # Variables
        repository : ProductRepository
        data       : Product
        # Code
        repository = self.__repository
        data = repository.selectByIdAndRestaurant( id, restaurantId )
        if data is None:
            raise ProductNotFoundException( id )
        return data
    
    def findByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> Product:
        # Variables
        repository : ProductRepository
        data       : Product
        # Code
        repository = self.__repository
        data = repository.selectByNameAndRestaurant( name, restaurantId )
        if data is None:
            raise ProductNameNotFoundException( name )
        return data