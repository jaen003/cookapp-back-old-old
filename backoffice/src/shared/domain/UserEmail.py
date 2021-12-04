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

class UserEmail( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str = None ) -> None:
        super().__init__( value )