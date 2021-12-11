"""
 *
 * Libraries 
 *
"""

from src.table.domain  import TableDescription
from src.shared.domain import TableId
from src.shared.domain import RestaurantId
from src.table.domain  import TableRepository
from src.table.domain  import Table
from src.table.domain  import TableNotFoundException
from src.shared.domain import ServerInternalErrorException
from src.table.domain  import TableFinder
from src.shared.domain import EventBus

"""
 *
 * Classes 
 *
"""

class TableRewriter:

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

    def rewrite( 
        self, 
        id           : TableId,
        description  : TableDescription,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        table      : Table
        repository : TableRepository
        finder     : TableFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = TableFinder( repository )
        table      = finder.findByIdAndRestaurant( id, restaurantId )
        if table is None:
            raise TableNotFoundException( id )
        table.rewrite( description )
        if not repository.update( table ):
            raise ServerInternalErrorException()
        eventBus.publish( table.pullEvents() )
