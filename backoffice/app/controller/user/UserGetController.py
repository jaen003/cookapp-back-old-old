"""
 *
 * Libraries 
 *
"""

from flask                   import Blueprint
from flask                   import request
from src.user.application    import UserSearcher
from src.user.infrastructure import UserMysqlRepository
from src.shared.domain       import SERVER_ACCESS_DENIED
from src.user.infrastructure import UserTokenManager
from src.user.domain         import User

"""
 *
 * Global variables 
 *
"""

userGetController = Blueprint( 'userGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@userGetController.route( '/api/v1/user', methods = [ 'GET' ] )
def searchAllByRestaurant():
    # Variables
    responseCode    : int
    users           : list
    headers         : dict
    token           : str
    tokenManager    : UserTokenManager
    user            : User
    isAuthenticated : bool
    # Code
    headers         = request.headers
    tokenManager    = UserTokenManager()
    isAuthenticated = False
    try:
        token           = headers['Token']
        user            = tokenManager.decodeToken( token )
        isAuthenticated = user.role().isAdministrator()
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    searcher = UserSearcher( 
        repository = UserMysqlRepository(),
    )
    users, responseCode = searcher.searchAllByRestaurant(
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode, 'data' : users }, 202
