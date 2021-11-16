"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.user.application      import UserRenamer
from src.user.infrastructure   import UserMysqlRepository
from src.user.domain           import UserName
from src.shared.domain         import UserEmail
from src.shared.domain         import RestaurantId
from src.shared.infrastructure import EventBus
from src.shared.domain         import INCORRECT_DATA
from src.user.application      import UserRelocator
from src.user.domain           import UserRole
from src.user.application      import UserAuthenticator
from src.user.domain           import UserPassword
from src.user.infrastructure   import UserTokenManager
from src.user.application      import UserInsurer

"""
 *
 * Global variables 
 *
"""

userPutController = Blueprint( 'userPutController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToRename( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_name' ) is None:
        return False
    return True

def __isValidDataToRelocate( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_role' ) is None:
        return False
    return True

def __isValidDataToAuthenticate( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_password' ) is None:
        return False
    return True

def __isValidDataToInsure( data : dict ) -> bool:
    if data.get( 'user_password' ) is None:
        return False
    return True

@userPutController.route( '/api/v1/user/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data         : dict
    renamer      : UserRenamer
    responseCode : int
    # Code
    data    = request.json
    renamer = UserRenamer(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        email        = UserEmail( data.get( 'user_email' ) ),
        name         = UserName( data.get( 'user_name' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/relocate', methods = [ 'PUT' ] )
def relocate():
    # Variables
    data         : dict
    relocator    : UserRelocator
    responseCode : int
    # Code
    data    = request.json
    relocator = UserRelocator(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRelocate( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = relocator.relocate(
        email        = UserEmail( data.get( 'user_email' ) ),
        role         = UserRole( data.get( 'user_role' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/authenticate', methods = [ 'PUT' ] )
def authenticate():
    # Variables
    data          : dict
    authenticator : UserAuthenticator
    responseCode  : int
    response      : dict
    # Code
    data    = request.json
    authenticator = UserAuthenticator(
        repository   = UserMysqlRepository(),
        tokenManager = UserTokenManager(),
    )
    if not __isValidDataToAuthenticate( data ):
        return { 'code' : INCORRECT_DATA }, 202
    response, responseCode = authenticator.authenticate(
        email    = UserEmail( data.get( 'user_email' ) ),
        password = UserPassword( data.get( 'user_password' ) ),
    )
    return { 'code' : responseCode, 'data' : response }, 202

@userPutController.route( '/api/v1/user/insure', methods = [ 'PUT' ] )
def insure():
    # Variables
    data         : dict
    insurer      : UserInsurer
    responseCode : int
    # Code
    data    = request.json
    insurer = UserInsurer(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToInsure( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = insurer.insure(
        email    = UserEmail( 'jaenfelliniechavarriatijo@gmail.com' ),
        password = UserPassword( data.get( 'user_password' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202