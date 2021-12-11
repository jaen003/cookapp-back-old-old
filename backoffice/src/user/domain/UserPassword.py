"""
 *
 * Libraries 
 *
"""

import hashlib
from src.shared.domain             import StringValueObject
from random                        import choice
from .InvalidUserPasswordException import InvalidUserPasswordException

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
        if not self.isValid():
            raise InvalidUserPasswordException( value )
    
    @classmethod
    def weak( cls ): # -> UserPassword
        # Variables
        password : str
        # Code
        password = ''
        password = password.join( [ choice( cls.__ALLOWED_VALUES ) for i in range( cls.__SHORT_SIZE ) ] )
        self     = cls( password )
        return self
    
    @classmethod
    def encrypt( cls, value : str ): # -> UserPassword
        # Variables
        password : str
        encoded  = value.encode()
        password = hashlib.sha256( encoded ).hexdigest()
        self    = cls( password )
        return self
    
    def isValid( self ):
        if self.isLongerThan( self.__SHORT_SIZE - 1 ):
            return True
        return False