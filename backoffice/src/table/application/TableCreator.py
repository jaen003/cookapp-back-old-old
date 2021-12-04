"""
 *
 * Libraries 
 *
"""

from src.table.domain      import TableNumber
from src.table.domain      import TableDescription
from src.shared.domain     import TableId
from src.shared.domain     import RestaurantId
from src.table.domain      import TableRepository
from src.table.domain      import Table
from src.shared.domain     import SUCCESSFUL_REQUEST
from src.shared.domain     import SERVER_INTERNAL_ERROR
from src.shared.domain     import DomainException
from src.table.domain      import TableFinder
from src.shared.domain     import TABLE_ALREADY_CREATED
from src.shared.domain     import EventBus
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder

"""
 *
 * Classes 
 *
"""

class TableCreator:

    """
     *
     * Parameters 
     *
    """
 
    __repository           : TableRepository
    __restaurantRepository : RestaurantRepository
    __eventBus             : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : TableRepository,
        restaurantRepository : RestaurantRepository,
        eventBus             : EventBus,
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventBus             = eventBus

    def create( 
        self, 
        id           : TableId, 
        number       : TableNumber,
        description  : TableDescription,
        restaurantId : RestaurantId,
    ) -> int:
        # Variables
        table                : Table
        repository           : TableRepository
        finder               : TableFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = TableFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        try:
            table = Table.create( id, number, description, restaurantId )
            restaurantFinder.findById( restaurantId )
            try:            
                finder.findByNumberAndRestaurant( number, restaurantId )
                return TABLE_ALREADY_CREATED
            except DomainException:
                pass
            if repository.insert( table ):
                eventBus.publish( table.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
