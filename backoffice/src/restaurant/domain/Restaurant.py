"""
 *
 * Libraries 
 *
"""

from src.shared.domain               import AggregateRoot
from .RestaurantName                 import RestaurantName
from src.shared.domain               import RestaurantId
from .InvalidRestaurantNameException import InvalidRestaurantNameException
from .RestaurantStatus               import RestaurantStatus

"""
 *
 * Classes 
 *
"""

class Restaurant( AggregateRoot ):

    """
     *
     * Parameters 
     *
    """

    __id     : RestaurantId
    __name   : RestaurantName
    __status : RestaurantStatus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id     : RestaurantId,
        name   : RestaurantName,
        status : RestaurantStatus,
    ) -> None:
        self.__id     = id
        self.__name   = name
        self.__status = status
    
    @classmethod
    def create( cls ): # -> Restaurant
        self = cls( 
            id     = RestaurantId(),
            name   = None,
            status = RestaurantStatus.enabled(),
        )
        return self

    def id( self ) -> RestaurantId:
        return self.__id
    
    def name( self ) -> RestaurantName:
        return self.__name

    def status( self ) -> RestaurantStatus:
        return self.__status
    
    def rename( self, name : RestaurantName ) -> None:
        if name.isEmpty():
            raise InvalidRestaurantNameException( name )
        self.__name = name