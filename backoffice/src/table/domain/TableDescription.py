"""
 *
 * Libraries 
 *
"""

from src.shared.domain import StringValueObject

"""
 *
 * Classes 
 *
"""

class TableDescription( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str = None ) -> None:
        if value is None:
            value = 'No information'
        super().__init__( value )