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
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import SERVER_INTERNAL_ERROR
from src.shared.domain import DomainException
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
    ) -> int:
        # Variables
        table      : Table
        repository : TableRepository
        finder     : TableFinder
        eventBus   : EventBus
        # Code
        eventBus   = self.__eventBus
        repository = self.__repository
        finder     = TableFinder( repository )
        try:
            table = finder.findByIdAndRestaurant( id, restaurantId )
            table.rewrite( description )
            if repository.update( table ):
                eventBus.publish( table.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
