"""
 *
 * Libraries 
 *
"""

from .ProductName        import ProductName
from .ProductPrice       import ProductPrice
from .ProductDescription import ProductDescription
from src.shared.domain   import ProductId
from src.shared.domain   import RestaurantId
from src.shared.domain   import DomainEvent

"""
 *
 * Classes 
 *
"""

class ProductCreated( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id           : ProductId
    __name         : ProductName
    __price        : ProductPrice
    __description  : ProductDescription
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : ProductId          = None, 
        name         : ProductName        = None,
        price        : ProductPrice       = None,
        description  : ProductDescription = None,
        restaurantId : RestaurantId       = None,
    ) -> None:
        super().__init__( 'product_created' )
        self.__id           = id
        self.__name         = name
        self.__price        = price
        self.__description  = description
        self.__restaurantId = restaurantId
    
    def id( self ) -> ProductId:
        return self.__id
    
    def name( self ) -> ProductName:
        return self.__name
    
    def price( self ) -> ProductPrice:
        return self.__price

    def description( self ) -> ProductDescription:
        return self.__description
    
    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'         : self.uuid(),
            'occurredOn'   : str( self.occurredOn() ),
            'id'           : self.__id.value(),
            'name'         : self.__name.value(),
            'price'        : self.__price.value(),
            'description'  : self.__description.value(),
            'restaurantId' : self.__restaurantId.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid          = body['uuid']
        self._occurredOn    = int( body['occurredOn'] )
        self.__id           = ProductId( body['id'] )
        self.__name         = ProductName( body['name'] )
        self.__price        = ProductPrice( body['price'] )
        self.__description  = ProductDescription( body['description'] )
        self.__restaurantId = RestaurantId( body['restaurantId'] )

