"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserPassword
from src.shared.domain import UserEmail
from src.user.domain   import UserRepository
from src.user.domain   import User
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import DomainException
from src.user.domain   import UserFinder
from src.shared.domain import USER_DISABLED
from src.shared.domain import USER_BLOCKED
from src.shared.domain import INCORRECT_DATA
from src.user.domain   import UserTokenManager

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
    ) -> tuple[ dict, int ]:
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
        try:
            user = finder.findByEmail( email )
            if user.status().isDisabled():
                return response, USER_DISABLED
            if user.status().isBlocked():
                return response, USER_BLOCKED
            if not user.isAuthentic( password ):
                return response, INCORRECT_DATA
            token = tokenManager.generateToken( user )
            response['user_token'] = token
            response['user_role'] = user.role().value()
            return response, SUCCESSFUL_REQUEST
        except DomainException as exc:
            return response, exc.code()