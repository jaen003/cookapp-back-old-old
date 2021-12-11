"""
 *
 * Libraries 
 *
"""

from .StringValueObject         import StringValueObject
from .InvalidUserEmailException import InvalidUserEmailException

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
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidUserEmailException( value )