"""
 *
 * Libraries 
 *
"""

from .backofficeUserName                 import UserName
from src.shared.domain                   import UserEmail
from .backofficeUserPassword             import UserPassword
from .backofficeUserRole                 import UserRole
from src.shared.domain                   import RestaurantId
from src.shared.domain                   import AggregateRoot
from abc                                 import abstractmethod
from .backofficeUserDeleted              import UserDeleted
from .backofficeUserRenamed              import UserRenamed
from .backofficeUserRelocated            import UserRelocated
from .backofficeInvalidUserRoleException import InvalidUserRoleException

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
    ) -> None:
        super().__init__()
        self._email        = email
        self._name         = name
        self._password     = password
        self._role         = role
        self._status       = status
        self._restaurantId = restaurantId
    
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
    
    def reassure( self, password : UserPassword ) -> None:
        pass
    
    def relocate( self, role : UserRole ) -> None:
        if not role.isValid():
            raise InvalidUserRoleException( role )
        self._role = role
        self.record( UserRelocated(
            role  = role,
            email = self._email,
        ) )