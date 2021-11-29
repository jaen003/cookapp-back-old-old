"""
 *
 * Libraries 
 *
"""

import jwt
import os
from src.user.domain   import User
from src.user.domain   import UserRole
from src.shared.domain import UserEmail
from src.shared.domain import RestaurantId
from src.user.domain   import UserTokenManager as TokenManager

"""
 *
 * Interfaces
 *
"""

class UserTokenManager( TokenManager ):

    """
     *
     * Methods 
     *
    """
    
    def generateToken( self, user : User ) -> str:
        # Variables
        token  : str
        claims : dict
        secret : str
        # Code
        claims = {
            'email'        : user.email().value(),
            'role'         : user.role().value(),
            'restaurantId' : user.restaurantId().value(),
        }
        secret = os.getenv( 'SECRET_KEY' )
        token = jwt.encode( 
            claims, 
            secret, 
            algorithm ='HS256',
        )
        return token
    
    def decodeToken( self, token : str ) -> User:
        # Variables
        claims : dict
        secret : str
        user   : User
        # Code
        secret = os.getenv( 'SECRET_KEY' )
        claims = jwt.decode( token, secret, algorithms=['HS256'] )
        user = User(
            email        = UserEmail( claims['email'] ),
            name         = None,
            password     = None,
            role         = UserRole( claims['role'] ),
            status       = None,
            restaurantId = RestaurantId( claims['restaurantId'] ),
        )
        return user