"""
 *
 * Libraries 
 *
"""

from .StringValueObject import StringValueObject

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