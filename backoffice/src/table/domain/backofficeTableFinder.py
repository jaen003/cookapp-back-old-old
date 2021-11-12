"""
 *
 * Libraries 
 *
"""

from .backofficeTableNotFoundException       import TableNotFoundException
from .backofficeTableRepository              import TableRepository
from src.shared.domain                       import TableId
from src.shared.domain                       import RestaurantId
from .backofficeTable                        import Table 
from .backofficeTableNumber                  import TableNumber
from .backofficeTableNumberNotFoundException import TableNumberNotFoundException

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
        if data is None:
            raise TableNotFoundException( id )
        return data
    
    def findByNumberAndRestaurant( self, number : TableNumber, restaurantId : RestaurantId ) -> Table:
        # Variables
        repository : TableRepository
        data       : Table
        # Code
        repository = self.__repository
        data = repository.selectByNumberAndRestaurant( number, restaurantId )
        if data is None:
            raise TableNumberNotFoundException( number )
        return data