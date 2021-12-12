"""
 *
 * Libraries 
 *
"""

from .UserName                  import UserName
from src.shared.domain          import UserEmail
from .UserPassword              import UserPassword
from .UserRole                  import UserRole
from src.shared.domain          import RestaurantId
from src.shared.domain          import AggregateRoot
from .UserDeleted               import UserDeleted
from .UserRenamed               import UserRenamed
from .UserRelocated             import UserRelocated
from .UserInsured               import UserInsured
from .UserCode                  import UserCode
from .UserValidated             import UserValidated
from .UserStatus                import UserStatus
from .UserNotRelocatedException import UserNotRelocatedException

"""
 *
 * Classes 
 *
"""

class User( AggregateRoot ):

    """
     *
     * Parameters 
     *
    """

    __email        : UserEmail
    __name         : UserName
    __password     : UserPassword
    __role         : UserRole
    __status       : UserStatus
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
        status       : UserStatus,
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
    
    def status( self ) -> UserStatus:
        return self.__status

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def code( self ) -> UserCode:
        return self.__code

    def delete( self ) -> None:
        self.__status = UserStatus.deleted()
        self.record( UserDeleted(
            email = self.__email,
        ) )

    def rename( self, name : UserName ) -> None:
        self.__name = name
        self.record( UserRenamed(
            name  = name,
            email = self.__email,
        ) )
    
    def insure( self, password : UserPassword ) -> None:
        self.__password = password
        self.record( UserInsured(
            email    = self.__email,
            password = password,
        ) )

    def relocateAsChef( self ) -> None:
        if self.__role.isAdministrator():
            raise UserNotRelocatedException( self.__email )
        if self.__role.isWaiter():
            self.__role = UserRole.chef()
            self.record( UserRelocated(
                role  = self.__role,
                email = self.__email,
            ) )
    
    def relocateAsWaiter( self ) -> None:
        if self.__role.isAdministrator():
            raise UserNotRelocatedException( self.__email )
        if self.__role.isChef():
            self.__role = UserRole.waiter()
            self.record( UserRelocated(
                role  = self.__role,
                email = self.__email,
            ) )
            
    def validate( self, code : UserCode ) -> None:
        self.__code.match( code.value() )
        self.__status = UserStatus.enabled()
        self.record( UserValidated(
            email = self.__email,
        ) )
    
    def renovateCode( self, code : UserCode ) -> None:
        self.__code = code