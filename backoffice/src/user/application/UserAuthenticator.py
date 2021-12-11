"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserPassword
from src.shared.domain import UserEmail
from src.user.domain   import UserRepository
from src.user.domain   import User
from src.user.domain   import UserFinder
from src.user.domain   import UserTokenManager
from src.user.domain   import UserBlockedException
from src.user.domain   import UserDisabledException
from src.user.domain   import IncorrectUserDataException

"""
 *
 * Classes 
 *
"""

class UserAuthenticator:

    """
     *
     * Parameters 
     *
    """
 
    __repository   : UserRepository
    __tokenManager : UserTokenManager

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository   : UserRepository,
        tokenManager : UserTokenManager
    ) -> None:
        self.__repository   = repository
        self.__tokenManager = tokenManager

    def authenticate( 
        self, 
        email    : UserEmail,
        password : UserPassword,
    ) -> dict:
        # Variables
        user         : User
        repository   : UserRepository
        finder       : UserFinder
        tokenManager : UserTokenManager
        token        : str
        response     : dict
        # Code
        repository   = self.__repository
        finder       = UserFinder( repository )
        tokenManager = self.__tokenManager
        response     = {}
        user         = finder.findByEmail( email )
        if user is None:
            raise IncorrectUserDataException()
        if user.status().isDisabled():
            raise UserDisabledException( email )
        if user.status().isBlocked():
            raise UserBlockedException( email )
        if not user.password().equals( password.value() ):
            raise IncorrectUserDataException()
        token = tokenManager.generateToken( user )
        response['user_token'] = token
        response['user_role']  = user.role().value()
        return response