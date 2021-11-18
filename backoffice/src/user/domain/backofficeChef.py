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
from .backofficeUser                         import User
from .backofficeEmployeeCreated              import EmployeeCreated
from copy                                    import copy

"""
 *
 * Classes 
 *
"""

class Chef( User ):

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
    ): # -> User
        # Variables
        passwordDecrypted : UserPassword
        # Code
        if name.isEmpty():
            raise InvalidUserNameException( name )
        if email.isEmpty():
            raise InvalidUserEmailException( email )
        if password.isEmpty():
            raise InvalidUserPasswordException( password )
        passwordDecrypted = copy( password )
        password.encode()
        self = cls(
            email        = email,
            name         = name,
            password     = password,
            role         = UserRole.chef(),
            status       = cls._ENABLED,
            restaurantId = restaurantId,
        )
        self.record( EmployeeCreated(
            email        = email,
            name         = name,
            password     = passwordDecrypted,
            role         = self.role(),
            restaurantId = restaurantId,
        ) )
        return self
