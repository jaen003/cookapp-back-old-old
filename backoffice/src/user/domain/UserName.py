"""
 *
 * Libraries 
 *
"""

from src.shared.domain         import StringValueObject
from .InvalidUserNameException import InvalidUserNameException

"""
 *
 * Classes 
 *
"""

class UserName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidUserNameException( value )