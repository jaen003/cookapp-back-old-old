"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import IntValueObject
from .InvalidTableStatusException import InvalidTableStatusException

"""
 *
 * Classes 
 *
"""

class TableStatus( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __ENABLED = 1
    __DELETED = 2

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
        if not self.isValid():
            raise InvalidTableStatusException( value )
    
    @classmethod
    def enabled( cls ): # -> ProductStatus
        self = cls( cls.__ENABLED )
        return self
    
    @classmethod
    def deleted( cls ): # -> ProductStatus
        self = cls( cls.__DELETED )
        return self
    
    def isValid( self ) -> bool :
        if self.equals( self.__DELETED ) or self.equals( self.__ENABLED ):
            return True
        return False