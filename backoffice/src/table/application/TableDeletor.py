"""
 *
 * Libraries 
 *
"""

from src.table.domain  import TableRepository
from src.table.domain  import TableFinder
from src.table.domain  import Table
from src.shared.domain import TableId
from src.shared.domain import RestaurantId
from src.shared.domain import DomainException
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import SERVER_INTERNAL_ERROR
from src.shared.domain import EventBus

"""
 *
 * Classes 
 *
"""

class TableDeletor:

    """
     *
     * Parameters 
     *
    """

    __repository : TableRepository
    __eventBus   : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository : TableRepository,
        eventBus   : EventBus, 
    ) -> None:
        self.__repository = repository
        self.__eventBus   = eventBus
    
    def delete( 
        self,
        id           : TableId,
        restaurantId : RestaurantId,
    ) -> int:
        # Variables
        repository : TableRepository
        finder     : TableFinder
        table       : Table
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = TableFinder( repository )
        try:
            table = finder.findByIdAndRestaurant( id, restaurantId )
            table.delete()
            if repository.update( table ):
                eventBus.publish( table.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
