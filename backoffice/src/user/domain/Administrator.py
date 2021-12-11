"""
 *
 * Libraries 
 *
"""

from .UserName             import UserName
from src.shared.domain     import UserEmail
from .UserPassword         import UserPassword
from .UserRole             import UserRole
from src.shared.domain     import RestaurantId
from .AdministratorCreated import AdministratorCreated
from .User                 import User
from .UserCode             import UserCode
from .UserStatus           import UserStatus

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
    ): # -> User
        # Variables
        code : UserCode
        # Code
        code = UserCode.short()
        self = cls(
            email        = email,
            name         = name,
            password     = password,
            role         = UserRole.administrator(),
            status       = UserStatus.disabled(),
            restaurantId = restaurantId,
            code         = code,
        )
        self.record( AdministratorCreated(
            email        = email,
            name         = name,
            password     = password,
            restaurantId = restaurantId,
            code         = code,
        ) )
        return self
        
