"""
 *
 * Libraries 
 *
"""

from .backofficeUserName                     import UserName
from src.shared.domain                       import UserEmail
from .backofficeUserPassword                 import UserPassword
from .backofficeUserRole                     import UserRole
from src.shared.domain                       import RestaurantId
from .backofficeInvalidUserNameException     import InvalidUserNameException
from src.shared.domain                       import InvalidUserEmailException
from .backofficeInvalidUserPasswordException import InvalidUserPasswordException
from .backofficeAdministratorCreated         import AdministratorCreated
from .backofficeUser                         import User

"""
 *
 * Classes 
 *
"""

class Administrator( User ):

    """
     *
     * Methods 
     *
    """

    @classmethod
    def create(
        cls, 
        email        : UserEmail,
        name         : UserName,
        password     : UserPassword,
        restaurantId : RestaurantId,
        code         : str,
    ): # -> User
        if name.isEmpty():
            raise InvalidUserNameException( name )
        if email.isEmpty():
            raise InvalidUserEmailException( email )
        if password.isEmpty():
            raise InvalidUserPasswordException( password )
        self = cls(
            email        = email,
            name         = name,
            password     = password,
            role         = UserRole.administrator(),
            status       = cls._DISABLED,
            restaurantId = restaurantId,
        )
        self.record( AdministratorCreated(
            email        = email,
            name         = name,
            password     = password,
            restaurantId = restaurantId,
            code         = code,
        ) )
        return self
        
