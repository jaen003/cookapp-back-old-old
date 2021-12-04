"""
 *
 * Libraries 
 *
"""

from .ProductName                        import ProductName
from .ProductPrice                       import ProductPrice
from .ProductDescription                 import ProductDescription
from src.shared.domain                   import ProductId
from .InvalidProductNameException        import InvalidProductNameException
from src.shared.domain                   import InvalidProductIdException
from src.shared.domain                   import AggregateRoot
from .ProductCreated                     import ProductCreated
from .InvalidProductDescriptionException import InvalidProductDescriptionException
from .InvalidProductPriceException       import InvalidProductPriceException
from src.shared.domain                   import RestaurantId
from .ProductDeleted                     import ProductDeleted
from .ProductRenamed                     import ProductRenamed
from .ProductRevalued                    import ProductRevalued
from .ProductRewrited                    import ProductRewrited

"""
 *
 * Classes 
 *
"""

class Product( AggregateRoot ):

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

    __id           : ProductId
    __name         : ProductName
    __price        : ProductPrice
    __description  : ProductDescription
    __status       : int
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        status       : int,
        restaurantId : RestaurantId,
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__name         = name
        self.__price        = price
        self.__description  = description
        self.__status       = status
        self.__restaurantId = restaurantId

    def id( self ) -> ProductId:
        return self.__id
    
    def name( self ) -> ProductName:
        return self.__name

    def price( self ) -> ProductPrice:
        return self.__price
    
    def description( self ) -> ProductDescription:
        return self.__description

    def status( self ) -> int:
        return self.__status

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId

    @classmethod
    def create( 
        cls, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        restaurantId : RestaurantId,
    ): # -> Product
        if id.isEmpty():
            raise InvalidProductIdException( id )
        if name.isEmpty():
            raise InvalidProductNameException( name )
        if price.isValid() == False:
            raise InvalidProductPriceException( price )
        if description.isEmpty():
            raise InvalidProductDescriptionException( description )
        self = cls(
            id           = id,
            name         = name,
            price        = price,
            description  = description,
            status       = cls.__ENABLED,
            restaurantId = restaurantId,
        )
        self.record( ProductCreated(
            id           = id,
            name         = name,
            price        = price,
            description  = description,
            restaurantId = restaurantId,
        ) )
        return self    
    
    def delete( self ) -> None:
        self.__status = self.__DELETED
        self.record( ProductDeleted(
            id = self.__id,
        ) )
    
    def rename( self, name : ProductName ) -> None:
        if name.isEmpty():
            raise InvalidProductNameException( name )
        self.__name = name
        self.record( ProductRenamed(
            id   = self.__id,
            name = name,
        ) )
    
    def revalue( self, price : ProductPrice ) -> None:
        if not price.isValid():
            raise InvalidProductPriceException( price )
        self.__price = price
        self.record( ProductRevalued(
            id    = self.__id,
            price = price,
        ) )
    
    def rewrite( self, description : ProductDescription ) -> None:
        if description.isEmpty():
            raise InvalidProductDescriptionException( description )
        self.__description = description
        self.record( ProductRewrited(
            id          = self.__id,
            description = description,
        ) )