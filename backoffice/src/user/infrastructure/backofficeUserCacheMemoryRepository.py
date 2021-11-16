"""
 *
 * Libraries 
 *
"""

from time              import mktime
from src.user.domain   import User
from src.user.domain   import UserRepository
from src.shared.domain import UserEmail
from datetime          import datetime
from datetime          import timedelta

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
     * Consts 
     *
    """

    __VALIDATION_EXPIRATION_TIME = 5 # 5 minutes

    """
     *
     * Parameters 
     *
    """

    __users = dict

    """
     *
     * Methods 
     *
    """

    def __init__( self ):
        self.__users = {}

    def insert( self, user : User ) -> bool:
        # Variables
        expiresAt : int
        # Code
        dateNow   = datetime.now()
        finalDate = dateNow + timedelta( minutes = self.__VALIDATION_EXPIRATION_TIME )
        expiresAt = int( mktime( finalDate.timetuple() ) )
        self.__users[user.email().value()] = {
            'code'      : user.code(),
            'expiresAt' : expiresAt,
        }
    
    def selectByEmail( self, email : UserEmail ) -> User:
        # Variables
        expiresAt : int
        data      : dict
        user      : User
        # Code
        user      = None
        data      = self.__users[email.value()]
        if data is not None:
            dateNow   = int( mktime( datetime.now().timetuple() ) )
            expiresAt = data['expiresAt']
            if dateNow < expiresAt:
                user = User( 
                    email        = None,
                    name         = None,
                    password     = None,
                    role         = None,
                    status       = None,
                    restaurantId = None,
                    code         = data['code'],
                )
        return user


