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

    _email        : UserEmail
    _name         : UserName
    _password     : UserPassword
    _role         : UserRole
    _status       : int
    _restaurantId : RestaurantId
    _code         : str

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
        code         : str = None,
    ) -> None:
        super().__init__()
        self._email        = email
        self._name         = name
        self._password     = password
        self._role         = role
        self._status       = status
        self._restaurantId = restaurantId
        self._code         = code
    
    def email( self ) -> UserEmail:
        return self._email

    def name( self ) -> UserName:
        return self._name

    def password( self ) -> UserPassword:
        return self._password
        
    def role( self ) -> UserRole:
        return self._role
    
    def status( self ) -> int:
        return self._status

    def restaurantId( self ) -> RestaurantId:
        return self._restaurantId
    
    def code( self ) -> str:
        return self._code

    @abstractmethod
    def create( 
        self,
        email        : UserEmail,
        name         : UserName,
        password     : UserPassword,
        restaurantId : RestaurantId, 
    ): # -> User
        pass

    def delete( self ) -> None:
        self._status = self.__DELETED
        self.record( UserDeleted(
            email = self._email,
        ) )

    def rename( self, name : UserName ) -> None:
        if name.isEmpty():
            raise InvalidUserNameException( name )
        self._name = name
        self.record( UserRenamed(
            name  = name,
            email = self._email,
        ) )
    
    def insure( self, password : UserPassword ) -> None:
        if password.isEmpty():
            raise InvalidUserPasswordException( password )
        self._password = password
        self.record( UserInsured(
            email    = self._email,
            password = password,
        ) )
    
    def relocate( self, role : UserRole ) -> None:
        if not role.isValid():
            raise InvalidUserRoleException( role )
        self._role = role
        self.record( UserRelocated(
            role  = role,
            email = self._email,
        ) )
    
    def isDisabled( self ) -> bool:
        if self._status == self._DISABLED:
            return True
        return False
    
    def isBlocked( self ) -> bool:
        if self._status == self.__BLOCKED:
            return True
        return False
    
    def isAuthentic( self, password : UserPassword ) -> bool:
        if self._password.equals( password.value() ):
            return True
        return False
    
    def isValidated( self, code : str ) -> bool:
        if self._code == code:
            return True
        return False