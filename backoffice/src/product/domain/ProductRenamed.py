"""
 *
 * Libraries 
 *
"""

from .ProductName      import ProductName
from src.shared.domain import ProductId
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class ProductRenamed( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id   : ProductId
    __name : ProductName

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id   : ProductId   = None, 
        name : ProductName = None,
    ) -> None:
        super().__init__( 'product_renamed' )
        self.__id   = id
        self.__name = name
    
    def id( self ) -> ProductId:
        return self.__id
    
    def name( self ) -> ProductName:
        return self.__name
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'id'         : self.__id.value(),
            'name'       : self.__name.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__id        = ProductId( body['id'] )
        self.__name      = ProductName( body['name'] )

