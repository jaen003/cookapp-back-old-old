"""
 *
 * Libraries 
 *
"""

from abc             import abstractmethod
from .backofficeUser import User

"""
 *
 * Interfaces
 *
"""

class UserTokenManager:

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

    @abstractmethod
    def expireToken( self, token : str ) -> None:
        pass