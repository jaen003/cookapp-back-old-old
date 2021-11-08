"""
 *
 * Libraries 
 *
"""

from .backofficeStringValueObject import StringValueObject

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