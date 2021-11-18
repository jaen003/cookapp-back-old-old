"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.user.application          import UserCreator
from src.user.infrastructure       import UserMysqlRepository
from src.user.domain               import UserName
from src.user.domain               import UserPassword
from src.shared.domain             import UserEmail
from src.restaurant.infrastructure import RestaurantRepository
from src.shared.infrastructure     import EventBus
from src.shared.domain             import INCORRECT_DATA
from src.user.infrastructure       import UserCacheMemoryRepository
from src.shared.domain             import SERVER_ACCESS_DENIED
from src.user.infrastructure       import UserTokenManager
from src.user.domain               import User

"""
 *
 * Global variables 
 *
"""

userPostController = Blueprint( 'userPostController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToCreateAdministrator( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_name' ) is None:
        return False
    if data.get( 'user_password' ) is None:
        return False
    return True

def __isValidDataToCreateEmployee( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_name' ) is None:
        return False
    return True

@userPostController.route( '/api/v1/user/create/administrator', methods = [ 'POST' ] )
def createAdministrator():
    # Variables
    data            : dict
    creator         : UserCreator
    responseCode    : int
    # Code
    data    = request.json
    creator = UserCreator(
        repository           = UserMysqlRepository(),
        restaurantRepository = RestaurantRepository(),
        eventBus             = EventBus(),
        volatileRepository   = UserCacheMemoryRepository(),
    )
    if not __isValidDataToCreateAdministrator( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.createAdministrator(
        email    = UserEmail( data.get( 'user_email' ) ),
        name     = UserName( data.get( 'user_name' ) ),
        password = UserPassword( data.get( 'user_password' ) ),
    )
    return { 'code' : responseCode }, 202

@userPostController.route( '/api/v1/user/create/waiter', methods = [ 'POST' ] )
def createWaiter():
    # Variables
    data            : dict
    creator         : UserCreator
    responseCode    : int
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
    data    = request.json
    creator = UserCreator(
        repository           = UserMysqlRepository(),
        restaurantRepository = RestaurantRepository(),
        eventBus             = EventBus(),
    )
    if not __isValidDataToCreateEmployee( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.createWaiter(
        email        = UserEmail( data.get( 'user_email' ) ),
        name         = UserName( data.get( 'user_name' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@userPostController.route( '/api/v1/user/create/chef', methods = [ 'POST' ] )
def createChef():
    # Variables
    data            : dict
    creator         : UserCreator
    responseCode    : int
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
    data    = request.json
    creator = UserCreator(
        repository           = UserMysqlRepository(),
        restaurantRepository = RestaurantRepository(),
        eventBus             = EventBus(),
    )
    if not __isValidDataToCreateEmployee( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.createChef(
        email        = UserEmail( data.get( 'user_email' ) ),
        name         = UserName( data.get( 'user_name' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202