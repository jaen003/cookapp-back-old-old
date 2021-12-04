"""
 *
 * Libraries 
 *
"""

from abc               import abstractmethod
from abc               import ABCMeta
from .Product          import Product
from .ProductName      import ProductName
from src.shared.domain import ProductId
from src.shared.domain import RestaurantId

"""
 *
 * Interfaces
 *
"""

class ProductRepository( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def insert( self, product : Product ) -> bool:
        pass
    
    @abstractmethod
    def update( self, product : Product ) -> bool:
        pass
    
    @abstractmethod
    def selectByIdAndRestaurant( self, id : ProductId, restaurantId : RestaurantId ) -> Product:
        pass
    
    @abstractmethod
    def selectByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> Product:
        pass
    
    @abstractmethod
    def selectAllByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> list:
        pass
    
    @abstractmethod
    def selectAllByRestaurant( self, restaurantId : RestaurantId ) -> list:
        pass