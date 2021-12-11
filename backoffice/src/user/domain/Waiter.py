"""
 *
 * Libraries 
 *
"""

from .UserName         import UserName
from src.shared.domain import UserEmail
from .UserPassword     import UserPassword
from .UserRole         import UserRole
from src.shared.domain import RestaurantId
from .User             import User
from .EmployeeCreated  import EmployeeCreated
from .UserStatus       import UserStatus

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
        passwordEncrypted : UserPassword
        # Code
        passwordEncrypted = UserPassword.encrypt( password.value() )
        self = cls(
            email        = email,
            name         = name,
            password     = passwordEncrypted,
            role         = UserRole.waiter(),
            status       = UserStatus.enabled(),
            restaurantId = restaurantId,
        )
        self.record( EmployeeCreated(
            email        = email,
            name         = name,
            password     = password,
            role         = self.role(),
            restaurantId = restaurantId,
        ) )
        return self
