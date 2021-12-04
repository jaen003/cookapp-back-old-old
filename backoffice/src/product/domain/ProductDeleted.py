"""
 *
 * Libraries 
 *
"""

from src.shared.domain import ProductId
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class ProductDeleted( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id : ProductId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id : ProductId = None,
    ) -> None:
        super().__init__( 'product_deleted' )
        self.__id = id
    
    def id( self ) -> ProductId:
        return self.__id
    
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

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__id        = ProductId( body['id'] )

