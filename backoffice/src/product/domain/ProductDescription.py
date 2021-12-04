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

class ProductDescription( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )