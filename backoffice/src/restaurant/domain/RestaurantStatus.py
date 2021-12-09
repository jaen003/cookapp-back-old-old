"""
 *
 * Libraries 
 *
"""

from src.shared.domain                 import IntValueObject
from .InvalidRestaurantStatusException import InvalidRestaurantStatusException

"""
 *
 * Classes 
 *
"""

class RestaurantStatus( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __ENABLED = 1

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
        if not self.isValid():
            raise InvalidRestaurantStatusException( value )
    
    @classmethod
    def enabled( cls ): # -> RestaurantStatus
        self = cls( cls.__ENABLED )
        return self
    
    def isValid( self ) -> bool :
        if self.equals( self.__ENABLED ):
            return True
        return False