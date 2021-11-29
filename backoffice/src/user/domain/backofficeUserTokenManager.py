"""
 *
 * Libraries 
 *
"""

from abc             import abstractmethod
from .backofficeUser import User
from abc             import ABCMeta

"""
 *
 * Interfaces
 *
"""

class UserTokenManager( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def generateToken( self, user : User ) -> str:
        pass
    
    @abstractmethod
    def decodeToken( self, token : str ) -> User:
        pass