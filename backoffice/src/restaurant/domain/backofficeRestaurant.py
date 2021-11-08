"""
 *
 * Libraries 
 *
"""

from .backofficeRestaurantName import RestaurantName
from src.shared.domain         import RestaurantId

"""
 *
 * Classes 
 *
"""

class Restaurant:

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

    def id( self ) -> RestaurantId:
        return self.__id
    
    def name( self ) -> RestaurantName:
        return self.__name

    def status( self ) -> int:
        return self.__status