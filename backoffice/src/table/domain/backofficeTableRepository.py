"""
 *
 * Libraries 
 *
"""

from abc                    import abstractmethod
from .backofficeTable       import Table
from .backofficeTableNumber import TableNumber
from src.shared.domain      import TableId
from src.shared.domain      import RestaurantId


"""
 *
 * Interfaces
 *
"""

class TableRepository:

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def insert( self, table : Table ) -> bool:
        pass
    
    @abstractmethod
    def update( self, table : Table ) -> bool:
        pass
    
    @abstractmethod
    def selectByIdAndRestaurant( self, id : TableId, restaurantId : RestaurantId ) -> Table:
        pass
    
    @abstractmethod
    def selectByNumberAndRestaurant( self, number : TableNumber, restaurantId : RestaurantId ) -> Table:
        pass
    
    @abstractmethod
    def selectAllByRestaurant( self, restaurantId : RestaurantId ) -> list:
        pass