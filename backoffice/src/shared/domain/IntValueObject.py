"""
 *
 * Classes 
 *
"""

class IntValueObject:

    """
     *
     * Parameters 
     *
    """

    __value : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, value : int ) -> None:
        self.__value = value
    
    def value( self ) -> int:
        return self.__value
    
    def equals( self, value : int ) -> bool:
        if self.__value == value:
            return True
        return False
    
    def isLessThan( self, value : int ) -> bool:
        if self.__value < value:
            return True
        return False
    
    def isBiggerThan( self, value : int ) -> bool:
        if self.__value > value:
            return True
        return False
    
    def toString( self ) -> str:
        return str( self.__value )
