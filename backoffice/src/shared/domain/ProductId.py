"""
 *
 * Libraries 
 *
"""

from .StringValueObject         import StringValueObject
from .InvalidProductIdException import InvalidProductIdException

"""
 *
 * Classes 
 *
"""

class ProductId( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductIdException( id )