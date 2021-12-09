"""
 *
 * Libraries 
 *
"""

from src.shared.domain           import IntValueObject
from .InvalidUserStatusException import InvalidUserStatusException

"""
 *
 * Classes 
 *
"""

class UserStatus( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __ENABLED  = 1
    __DELETED  = 2
    __DISABLED = 3
    __BLOCKED  = 4

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
        if not self.isValid():
            raise InvalidUserStatusException( value )
    
    @classmethod
    def enabled( cls ): # -> ProductStatus
        self = cls( cls.__ENABLED )
        return self
    
    @classmethod
    def deleted( cls ): # -> ProductStatus
        self = cls( cls.__DELETED )
        return self
    
    @classmethod
    def blocked( cls ): # -> ProductStatus
        self = cls( cls.__BLOCKED )
        return self

    @classmethod
    def disabled( cls ): # -> ProductStatus
        self = cls( cls.__DISABLED )
        return self
    
    def isDisabled( self ) -> bool:
        if self.equals( self.__DISABLED ):
            return True
        return False
    
    def isBlocked( self ) -> bool:
        if self.equals( self.__BLOCKED ):
            return True
        return False
    
    def isValid( self ) -> bool :
        if self.equals( self.__DELETED ) or self.equals( self.__ENABLED ) or \
           self.equals( self.__BLOCKED ) or self.equals( self.__DISABLED ):
            return True
        return False