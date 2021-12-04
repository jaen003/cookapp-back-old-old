"""
 *
 * Libraries 
 *
"""

from .ProductDescription import ProductDescription
from src.shared.domain   import ProductId
from src.shared.domain   import DomainEvent

"""
 *
 * Classes 
 *
"""

class ProductRewrited( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id          : ProductId
    __description : ProductDescription

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id          : ProductId          = None, 
        description : ProductDescription = None,
    ) -> None:
        super().__init__( 'product_rewrited' )
        self.__id          = id
        self.__description = description
    
    def id( self ) -> ProductId:
        return self.__id
    
    def description( self ) -> ProductDescription:
        return self.__description
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'        : self.uuid(),
            'occurredOn'  : str( self.occurredOn() ),
            'id'          : self.__id.value(),
            'description' : self.__description.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid         = body['uuid']
        self._occurredOn   = int( body['occurredOn'] )
        self.__id          = ProductId( body['id'] )
        self.__description = ProductDescription( body['description'] )

