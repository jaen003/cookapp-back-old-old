"""
 *
 * Libraries 
 *
"""

from .backofficeUuidValueObject import UuidValueObject

"""
 *
 * Classes 
 *
"""

class RestaurantId( UuidValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str = None ) -> None:
        super().__init__( value )