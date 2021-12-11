"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import StringValueObject
from .InvalidProductNameException import InvalidProductNameException

"""
 *
 * Classes 
 *
"""

class ProductName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductNameException( value )