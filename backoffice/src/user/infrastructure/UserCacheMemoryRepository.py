"""
 *
 * Libraries 
 *
"""

from src.user.domain   import User
from src.user.domain   import UserRepository
from src.shared.domain import UserEmail
from src.user.domain   import UserName
from src.user.domain   import UserPassword
from src.user.domain   import UserRole
from src.user.domain   import UserCode
from src.shared.domain import RestaurantId
from src.user.domain   import UserStatus

"""
 *
 * Classes 
 *
"""

class Singleton( type ):

    """
     *
     * Parameters 
     *
    """

    __instances = {}

    """
     *
     * Methods 
     *
    """

    def __call__( cls, *args, **kwargs ):
        if cls not in cls.__instances:
            instance = super().__call__( *args, **kwargs )
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class UserCacheMemoryRepository( UserRepository, metaclass = Singleton ):

    """
     *
     * Parameters 
     *
    """

    __users : dict

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        self.__users = {}

    def insert( self, user : User ) -> bool:
        self.__users[user.email().value()] = {
            'name'         : user.name().value(),
            'code'         : user.code().value(),
            'password'     : user.password().value(),
            'role'         : user.role().value(),
            'status'       : user.status().value(),
            'restaurantId' : user.restaurantId().value(),
        }
        return True
    
    def update( self, user : User ) -> bool:
        self.__users[user.email().value()] = {
            'name'         : user.name().value(),
            'code'         : user.code().value(),
            'password'     : user.password().value(),
            'role'         : user.role().value(),
            'status'       : user.status().value(),
            'restaurantId' : user.restaurantId().value(),
        }
        return True
    
    def selectByEmail( self, email : UserEmail ) -> User:
        # Variables
        data : dict
        user : User
        # Code
        user = None
        if email.value() in self.__users:
            data = self.__users[email.value()]
            user = User( 
                email        = email,
                name         = UserName( data['name'] ),
                password     = UserPassword( data['password'] ),
                role         = UserRole( data['role'] ),
                status       = UserStatus( data['status'] ),
                restaurantId = RestaurantId( data['restaurantId'] ),
                code         = UserCode( data['code'] ),
            )                
        return user


