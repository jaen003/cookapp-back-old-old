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
from src.shared.domain                       import AggregateRoot
from abc                                     import abstractmethod
from .backofficeUserDeleted                  import UserDeleted
from .backofficeUserRenamed                  import UserRenamed
from .backofficeUserRelocated                import UserRelocated
from .backofficeInvalidUserRoleException     import InvalidUserRoleException
from .backofficeInvalidUserNameException     import InvalidUserNameException
from .backofficeUserInsured                  import UserInsured
from .backofficeInvalidUserPasswordException import InvalidUserPasswordException
from .backofficeUserCode                     import UserCode
from .backofficeUserValidated                import UserValidated
from .backofficeInvalidUserCodeException     import InvalidUserCodeException

"""
 *
 * Classes 
 *
"""

class User( AggregateRoot ):

    """
     *
     * Consts 
     *
    """

    _ENABLED  = 1
    __DELETED = 2
    _DISABLED = 3
    __BLOCKED = 4

    """
     *
     * Parameters 
     *
    """

    __email        : UserEmail
    __name         : UserName
    __password     : UserPassword
    __role         : UserRole
    __status       : int
    __restaurantId : RestaurantId
    __code         : UserCode

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        email        : UserEmail,
        name         : UserName,
        password     : UserPassword,
        role         : UserRole,
        status       : int,
        restaurantId : RestaurantId,
        code         : UserCode = None,
    ) -> None:
        super().__init__()
        self.__email        = email
        self.__name         = name
        self.__password     = password
        self.__role         = role
        self.__status       = status
        self.__restaurantId = restaurantId
        self.__code         = code
    
    def email( self ) -> UserEmail:
        return self.__email

    def name( self ) -> UserName:
        return self.__name

    def password( self ) -> UserPassword:
        return self.__password
        
    def role( self ) -> UserRole:
        return self.__role
    
    def status( self ) -> int:
        return self.__status

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def code( self ) -> UserCode:
        return self.__code

    def delete( self ) -> None:
        self.__status = self.__DELETED
        self.record( UserDeleted(
            email = self.__email,
        ) )

    def rename( self, name : UserName ) -> None:
        if name.isEmpty():
            raise InvalidUserNameException( name )
        self.__name = name
        self.record( UserRenamed(
            name  = name,
            email = self.__email,
        ) )
    
    def insure( self, password : UserPassword ) -> None:
        if password.isEmpty():
            raise InvalidUserPasswordException( password )
        self.__password = password
        self.record( UserInsured(
            email    = self.__email,
            password = password,
        ) )
    
    def relocate( self, role : UserRole ) -> None:
        if not role.isValid():
            raise InvalidUserRoleException( role )
        self.__role = role
        self.record( UserRelocated(
            role  = role,
            email = self.__email,
        ) )
    
    def isDisabled( self ) -> bool:
        if self.__status == self._DISABLED:
            return True
        return False
    
    def isBlocked( self ) -> bool:
        if self.__status == self.__BLOCKED:
            return True
        return False
    
    def isAuthentic( self, password : UserPassword ) -> bool:
        if self.__password.equals( password.value() ):
            return True
        return False
    
    def validate( self, code : UserCode ) -> None:
        if not self.__code.validate( code.value() ):
            raise InvalidUserCodeException( code )
        self.__status = self._ENABLED
        self.record( UserValidated(
            email = self.__email,
        ) )