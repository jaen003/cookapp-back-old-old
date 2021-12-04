"""
 *
 * Libraries 
 *
"""

from .TableNumber                 import TableNumber
from .TableDescription            import TableDescription
from src.shared.domain            import TableId
from src.shared.domain            import RestaurantId
from src.shared.domain            import InvalidTableIdException
from src.shared.domain            import AggregateRoot
from .TableCreated                import TableCreated
from .InvalidTableNumberException import InvalidTableNumberException
from .TableDeleted                import TableDeleted
from .TableRenumbered             import TableRenumbered
from .TableRewrited               import TableRewrited

"""
 *
 * Classes 
 *
"""

class Table( AggregateRoot ):

    """
     *
     * Consts 
     *
    """

    __ENABLED = 1
    __DELETED = 2

    """
     *
     * Parameters 
     *
    """

    __id           : TableId
    __number       : TableNumber
    __description  : TableDescription
    __status       : int
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
        status       : int,
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

    def status( self ) -> int:
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
        if id.isEmpty():
            raise InvalidTableIdException( id )
        if not number.isValid():
            raise InvalidTableNumberException( number )
        self = cls(
            id           = id,
            number       = number,
            description  = description,
            status       = cls.__ENABLED,
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
        self.__status = self.__DELETED
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