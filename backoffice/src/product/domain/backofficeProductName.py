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

class ProductName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )