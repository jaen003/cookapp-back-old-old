"""
 *
 * Libraries 
 *
"""

from .TableNumber      import TableNumber
from .TableDescription import TableDescription
from src.shared.domain import TableId
from src.shared.domain import RestaurantId
from src.shared.domain import AggregateRoot
from .TableCreated     import TableCreated
from .TableDeleted     import TableDeleted
from .TableRenumbered  import TableRenumbered
from .TableRewrited    import TableRewrited
from .TableStatus      import TableStatus

"""
 *
 * Classes 
 *
"""

class Table( AggregateRoot ):

    """
     *
     * Parameters 
     *
    """

    __id           : TableId
    __number       : TableNumber
    __description  : TableDescription
    __status       : TableStatus
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : TableId, 
        number       : TableNumber,
        description  : TableDescription,
        status       : TableStatus,
        restaurantId : RestaurantId,
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__number       = number
        self.__description   = description
        self.__status       = status
        self.__restaurantId = restaurantId

    def id( self ) -> TableId:
        return self.__id
    
    def number( self ) -> TableNumber:
        return self.__number
    
    def description( self ) -> TableDescription:
        return self.__description

    def status( self ) -> TableStatus:
        return self.__status

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    @classmethod
    def create( 
        cls, 
        id           : TableId,
        number       : TableNumber,        
        description  : TableDescription,
        restaurantId : RestaurantId,
    ): # -> Table
        self = cls(
            id           = id,
            number       = number,
            description  = description,
            status       = TableStatus.enabled(),
            restaurantId = restaurantId,
        )
        self.record( TableCreated(
            id           = id,
            number       = number,
            description  = description,
            restaurantId = restaurantId,
        ) )
        return self
    
    def delete( self ) -> None:
        self.__status = TableStatus.deleted()
        self.record( TableDeleted(
            id = self.__id,
        ) )
    
    def renumber( self, number : TableNumber ) -> None:
        self.__number = number
        self.record( TableRenumbered(
            id     = self.__id,
            number = number,
        ) )
    
    def rewrite( self, description : TableDescription ) -> None:
        self.__description = description
        self.record( TableRewrited(
            id          = self.__id,
            description = description,
        ) )