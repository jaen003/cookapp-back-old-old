"""
 *
 * Libraries 
 *
"""

from .backofficeTableNumber      import TableNumber
from .backofficeTableDescription import TableDescription
from src.shared.domain           import TableId
from src.shared.domain           import RestaurantId
from src.shared.domain           import DomainEvent

"""
 *
 * Classes 
 *
"""

class TableRenumbered( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id     : TableId
    __number : TableNumber

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id     : TableId, 
        number : TableNumber,
    ) -> None:
        super().__init__( 'table_renumbered' )
        self.__id     = id
        self.__number = number
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'id'         : self.__id.value(),
            'number'     : self.__number.value(),
        }
        return body
    
    def id( self ) -> TableId:
        return self.__id
    
    def number( self ) -> TableNumber:
        return self.__number

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__id        = TableId( body['id'] )
        self.__number    = TableName( body['number'] )

