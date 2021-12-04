"""
 *
 * Libraries 
 *
"""

from .TableDescription import TableDescription
from src.shared.domain import TableId
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class TableRewrited( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id         : TableId
    __decription : TableDescription

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id          : TableId          = None,
        description : TableDescription = None,
    ) -> None:
        super().__init__( 'table_rewrited' )
        self.__id         = id
        self.__decription = description
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'        : self.uuid(),
            'occurredOn'  : str( self.occurredOn() ),
            'id'          : self.__id.value(),
            'description' : self.__decription.value(),
        }
        return body
    
    def id( self ) -> TableId:
        return self.__id
    
    def description( self ) -> TableDescription:
        return self.__decription

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid        = body['uuid']
        self._occurredOn  = int( body['occurredOn'] )
        self.__id         = TableId( body['id'] )
        self.__decription = TableDescription( body['description'] )

