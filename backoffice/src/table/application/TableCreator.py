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
from src.table.domain      import TableFinder
from src.shared.domain     import ServerInternalErrorException
from src.table.domain      import TableNumberAlreadyCreatedException
from src.shared.domain     import EventBus
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantFinder
from src.restaurant.domain import RestaurantNotFoundException
from src.restaurant.domain import Restaurant

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
    ) -> None:
        # Variables
        table                : Table
        repository           : TableRepository
        finder               : TableFinder
        eventBus             : EventBus
        restaurantRepository : RestaurantRepository
        restaurantFinder     : RestaurantFinder
        restaurant           : Restaurant
        # Code
        eventBus             = self.__eventBus
        repository           = self.__repository
        finder               = TableFinder( repository )
        restaurantRepository = self.__restaurantRepository
        restaurantFinder     = RestaurantFinder( restaurantRepository )
        restaurant           = restaurantFinder.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        table = finder.findByNumberAndRestaurant( number, restaurantId ) 
        if table is not None:
            raise TableNumberAlreadyCreatedException( number )
        table = Table.create( id, number, description, restaurantId )
        if not repository.insert( table ):
            raise ServerInternalErrorException()
        eventBus.publish( table.pullEvents() )
