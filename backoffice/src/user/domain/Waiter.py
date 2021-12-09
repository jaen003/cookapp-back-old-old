"""
 *
 * Libraries 
 *
"""

from .UserName                     import UserName
from src.shared.domain             import UserEmail
from .UserPassword                 import UserPassword
from .UserRole                     import UserRole
from src.shared.domain             import RestaurantId
from .InvalidUserNameException     import InvalidUserNameException
from src.shared.domain             import InvalidUserEmailException
from .InvalidUserPasswordException import InvalidUserPasswordException
from .User                         import User
from .EmployeeCreated              import EmployeeCreated
from copy                          import copy
from .UserStatus                   import UserStatus

"""
 *
 * Classes 
 *
"""

class Waiter( User ):

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
            role         = UserRole.waiter(),
            status       = UserStatus.enabled(),
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
