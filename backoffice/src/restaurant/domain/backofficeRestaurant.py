"""
 *
 * Libraries 
 *
"""

from src.shared.domain                         import AggregateRoot
from .backofficeRestaurantName                 import RestaurantName
from src.shared.domain                         import RestaurantId
from .backofficeInvalidRestaurantNameException import InvalidRestaurantNameException

"""
 *
 * Classes 
 *
"""

class Restaurant( AggregateRoot ):

    """
     *
     * Consts 
     *
    """

    __ENABLED  = 1

    """
     *
     * Parameters 
     *
    """

    __id     : RestaurantId
    __name   : RestaurantName
    __status : int

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id     : RestaurantId,
        name   : RestaurantName,
        status : int,
    ) -> None:
        self.__id     = id
        self.__name   = name
        self.__status = status
    
    @classmethod
    def create( cls ): # -> Restaurant
        self = cls( 
            id     = RestaurantId(),
            name   = None,
            status = cls.__ENABLED,
        )
        return self

    def id( self ) -> RestaurantId:
        return self.__id
    
    def name( self ) -> RestaurantName:
        return self.__name

    def status( self ) -> int:
        return self.__status
    
    def rename( self, name : RestaurantName ) -> None:
        if name.isEmpty():
            raise InvalidRestaurantNameException( name )
        self.__name = name