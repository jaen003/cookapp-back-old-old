"""
 *
 * Libraries 
 *
"""

from .TableRepository  import TableRepository
from src.shared.domain import TableId
from src.shared.domain import RestaurantId
from .Table            import Table 
from .TableNumber      import TableNumber

"""
 *
 * Classes
 *
"""

class TableFinder:

    """
     *
     * Parameters 
     *
    """

    __repository : TableRepository

    """
     *
     * Methods 
     *
    """

    def __init__( self, repository : TableRepository ) -> None:
        self.__repository = repository
    
    def findByIdAndRestaurant( self, id : TableId, restaurantId : RestaurantId ) -> Table:
        # Variables
        repository : TableRepository
        data       : Table
        # Code
        repository = self.__repository
        data = repository.selectByIdAndRestaurant( id, restaurantId )
        return data
    
    def findByNumberAndRestaurant( self, number : TableNumber, restaurantId : RestaurantId ) -> Table:
        # Variables
        repository : TableRepository
        data       : Table
        # Code
        repository = self.__repository
        data = repository.selectByNumberAndRestaurant( number, restaurantId )
        return data