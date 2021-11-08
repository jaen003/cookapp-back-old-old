"""
 *
 * Libraries 
 *
"""

from .backofficeProductName                        import ProductName
from .backofficeProductPrice                       import ProductPrice
from .backofficeProductDescription                 import ProductDescription
from src.shared.domain                             import ProductId
from .backofficeInvalidProductNameException        import InvalidProductNameException
from src.shared.domain                             import InvalidProductIdException
from src.shared.domain                             import AggregateRoot
from .backofficeProductCreated                     import ProductCreated
from .backofficeInvalidProductDescriptionException import InvalidProductDescriptionException
from .backofficeInvalidProductPriceException       import InvalidProductPriceException
from src.shared.domain                             import RestaurantId

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
    
    @classmethod
    def create( 
        cls, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        restaurantId : RestaurantId,
    ): # -> Product
        cls.__validateDataToCreate( id, name, price, description )
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
    
    @staticmethod
    def __validateDataToCreate(
        id          : ProductId, 
        name        : ProductName,
        price       : ProductPrice,
        description : ProductDescription,
    ) -> None:
        if id.isEmpty():
            raise InvalidProductIdException()
        if name.isEmpty():
            raise InvalidProductNameException()
        if price.isValid() == False:
            raise InvalidProductPriceException()
        if description.isEmpty():
            raise InvalidProductDescriptionException()