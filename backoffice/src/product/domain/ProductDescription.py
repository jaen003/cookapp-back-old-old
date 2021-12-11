"""
 *
 * Libraries 
 *
"""

from src.shared.domain                   import StringValueObject
from .InvalidProductDescriptionException import InvalidProductDescriptionException

"""
 *
 * Classes 
 *
"""

class ProductDescription( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductDescriptionException( value )