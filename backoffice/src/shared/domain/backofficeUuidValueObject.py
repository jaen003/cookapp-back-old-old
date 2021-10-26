"""
 *
 * Libraries 
 *
"""

from uuid import uuid4

"""
 *
 * Classes 
 *
"""

class UuidValueObject:

    """
     *
     * Parameters 
     *
    """

    __value : str

    """
     *
     * Methods 
     *
    """

    def __init__( self, value : str ) -> None:
        self.__value = value
    
    @classmethod
    def random( cls ): # -> UuidValueObject
        self = cls( str( uuid4() ) )
        return self
    
    def value( self ) -> str:
        return self.__value

    def isEmpty( self ) -> bool:
        if self.__value == '':
            return True
        return False
    
    def equals( self, value : str ) -> bool:
        if self.__value == value:
            return True
        return False
