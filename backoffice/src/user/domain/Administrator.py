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
from .AdministratorCreated         import AdministratorCreated
from .User                         import User
from .UserCode                     import UserCode

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
        code         : UserCode,
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
        
