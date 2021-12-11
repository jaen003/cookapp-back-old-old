"""
 *
 * Libraries 
 *
"""

from src.table.domain  import TableNumber
from src.shared.domain import TableId
from src.shared.domain import RestaurantId
from src.table.domain  import TableRepository
from src.table.domain  import Table
from src.table.domain  import TableFinder
from src.shared.domain import EventBus
from src.table.domain  import TableNumberAlreadyCreatedException
from src.table.domain  import TableNotFoundException
from src.shared.domain import ServerInternalErrorException

"""
 *
 * Classes 
 *
"""

class TableRenumerator:

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

    def renumber( 
        self, 
        id           : TableId, 
        number       : TableNumber,
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
        table      = finder.findByNumberAndRestaurant( number, restaurantId )
        if table is not None:
            raise TableNumberAlreadyCreatedException( number )
        table = finder.findByIdAndRestaurant( id, restaurantId )
        if table is None:
            raise TableNotFoundException( id )
        table.renumber( number )
        if not repository.update( table ):
            raise ServerInternalErrorException()
        eventBus.publish( table.pullEvents() )
