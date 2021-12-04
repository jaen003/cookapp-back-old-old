"""
 *
 * Libraries 
 *
"""

from src.table.domain  import TableRepository
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import RestaurantId

"""
 *
 * Classes 
 *
"""

class TableSearcher:

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

    def searchAllByRestaurant( 
        self,
        restaurantId : RestaurantId,
    ) -> tuple[ list, int ]:
        # Variables
        repository : TableRepository
        tables   : list
        # Code
        repository = self.__repository
        tables     = repository.selectAllByRestaurant( restaurantId )
        return tables, SUCCESSFUL_REQUEST
