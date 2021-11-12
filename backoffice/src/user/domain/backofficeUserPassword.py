"""
 *
 * Libraries 
 *
"""

import hashlib
from src.shared.domain import StringValueObject
from random            import choice

"""
 *
 * Classes 
 *
"""

class UserPassword( StringValueObject ):

    """
     *
     * Consts 
     *
    """

    __ALLOWED_VALUES = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-&+'
    __SHORT_SIZE     = 8

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
    
    @classmethod
    def short( cls ): # -> StringValueObject
        # Variables
        password : str
        # Code
        password = ''
        password = password.join( [ choice( cls.__ALLOWED_VALUES ) for i in range( cls.__SHORT_SIZE ) ] )
        self = cls( password )
        return self
    
    def encode( self ) -> None:
        encoded = self._value.encode()
        self._value = hashlib.sha256( encoded ).hexdigest()