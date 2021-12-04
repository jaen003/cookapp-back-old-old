"""
 *
 * Libraries 
 *
"""

from src.shared.domain import TableId
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class TableDeleted( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id : TableId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id : TableId = None,
    ) -> None:
        super().__init__( 'table_deleted' )
        self.__id = id
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'id'         : self.__id.value(),
        }
        return body
    
    def id( self ) -> TableId:
        return self.__id

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__id        = TableId( body['id'] )

