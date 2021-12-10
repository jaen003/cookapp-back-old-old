"""
 *
 * Libraries 
 *
"""

import jwt
import os
from src.user.domain      import User
from src.shared.domain    import UserEmail
from src.user.domain      import UserTokenManager
from .UserMysqlRepository import UserMysqlRepository
from datetime             import datetime
from time                 import mktime
from datetime             import timedelta

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

class UserTokenManagerAdapter( UserTokenManager, metaclass = Singleton ):

    """
     *
     * Consts 
     *
    """

    __EXPIRATION_TIME = 24 # 24 hours

    """
     *
     * Parameters 
     *
    """

    __allowedTokens : list[ str ]

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        self.__allowedTokens = []
    
    def generateToken( self, user : User ) -> str:
        # Variables
        token     : str
        claims    : dict
        secret    : str
        expiresAt : int
        # Code
        dateNow   = datetime.now()
        finalDate = dateNow + timedelta( hours = self.__EXPIRATION_TIME )
        expiresAt = int( mktime( finalDate.timetuple() ) )
        claims = { 
            'email'     : user.email().value(),
            'expiresAt' : expiresAt,
        }
        secret = os.getenv( 'SECRET_KEY' )
        token = jwt.encode( 
            claims, 
            secret, 
            algorithm ='HS256',
        )
        self.__allowedTokens.append( token )
        return token
    
    def decodeToken( self, token : str ) -> User:
        # Variables
        claims              : dict
        secret              : str
        user                : User
        userMysqlRepository : UserMysqlRepository
        email               : UserEmail
        expiresAt           : int
        # Code
        if not token in self.__allowedTokens:
            return None
        userMysqlRepository = UserMysqlRepository()
        secret    = os.getenv( 'SECRET_KEY' )
        claims    = jwt.decode( token, secret, algorithms=['HS256'] )
        dateNow   = int( mktime( datetime.now().timetuple() ) )
        expiresAt = claims['expiresAt']
        if dateNow > expiresAt:
            self.__allowedTokens.remove( token )
            return None
        email     = UserEmail( claims['email'] )
        user      = userMysqlRepository.selectByEmail( email )
        if user.isDisabled() or user.isBlocked():
            return None
        return user
    
    def expireToken( self, token : str ) -> None:
        if token in self.__allowedTokens:
            self.__allowedTokens.remove( token )