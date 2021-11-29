"""
 *
 * Classes 
 *
"""

class StringValueObject:

    """
     *
     * Parameters 
     *
    """

    _value : str

    """
     *
     * Methods 
     *
    """

    def __init__( self, value : str ) -> None:
        self._value = value
    
    def value( self ) -> str:
        return self._value

    def isEmpty( self ) -> bool:
        if self._value == '':
            return True
        return False
    
    def equals( self, value : str ) -> bool:
        if self._value == value:
            return True
        return False
