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

class RestaurantId( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )