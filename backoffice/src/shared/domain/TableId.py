"""
 *
 * Libraries 
 *
"""

from .StringValueObject       import StringValueObject
from .InvalidTableIdException import InvalidTableIdException

"""
 *
 * Classes 
 *
"""

class TableId( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidTableIdException( value )
