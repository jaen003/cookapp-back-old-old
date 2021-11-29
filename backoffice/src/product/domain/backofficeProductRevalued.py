"""
 *
 * Libraries 
 *
"""

from .backofficeProductPrice import ProductPrice
from src.shared.domain       import ProductId
from src.shared.domain       import DomainEvent

"""
 *
 * Classes 
 *
"""

class ProductRevalued( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id    : ProductId
    __price : ProductPrice

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id    : ProductId    = None,
        price : ProductPrice = None,
    ) -> None:
        super().__init__( 'product_revalued' )
        self.__id    = id
        self.__price = price
    
    def id( self ) -> ProductId:
        return self.__id
    
    def price( self ) -> ProductPrice:
        return self.__price
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'id'         : self.__id.value(),
            'price'      : self.__price.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__id        = ProductId( body['id'] )
        self.__price     = ProductPrice( body['price'] )

