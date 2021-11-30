"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.user.infrastructure   import UserCacheMemoryRepository
from src.user.application      import UserRenamer
from src.user.infrastructure   import UserMysqlRepository
from src.user.domain           import UserName
from src.shared.domain         import UserEmail
from src.shared.infrastructure import EventBus
from src.shared.domain         import INCORRECT_DATA
from src.user.application      import UserRelocator
from src.user.domain           import UserRole
from src.user.application      import UserAuthenticator
from src.user.domain           import UserPassword
from src.user.infrastructure   import UserTokenManager
from src.user.application      import UserInsurer
from src.user.application      import UserValidator
from src.user.domain           import UserCode
from src.shared.infrastructure import EmailSender
from src.user.application      import UserRenovator
from src.shared.domain         import SERVER_ACCESS_DENIED
from src.user.infrastructure   import UserTokenManager
from src.user.domain           import User

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

def __isValidDataToValidate( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_code' ) is None:
        return False
    return True

def __isValidDataToRenovateCode( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    return True

@userPutController.route( '/api/v1/user/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data            : dict
    renamer         : UserRenamer
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
    renamer = UserRenamer(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        email        = UserEmail( data.get( 'user_email' ) ),
        name         = UserName( data.get( 'user_name' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/relocate', methods = [ 'PUT' ] )
def relocate():
    # Variables
    data            : dict
    relocator       : UserRelocator
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
    relocator = UserRelocator(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRelocate( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = relocator.relocate(
        email        = UserEmail( data.get( 'user_email' ) ),
        role         = UserRole( data.get( 'user_role' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/login', methods = [ 'PUT' ] )
def login():
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

@userPutController.route( '/api/v1/user/logout', methods = [ 'PUT' ] )
def logout():
    # Variables
    token        : str
    tokenManager : UserTokenManager
    # Code
    headers      = request.headers
    tokenManager = UserTokenManager()
    try:
        token = headers['Token']
        tokenManager.expireToken( token )
    except:
        pass
    return {}, 204

@userPutController.route( '/api/v1/user/insure', methods = [ 'PUT' ] )
def insure():
    # Variables
    data            : dict
    insurer         : UserInsurer
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
        isAuthenticated = True
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    data    = request.json
    insurer = UserInsurer(
        repository = UserMysqlRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToInsure( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = insurer.insure(
        email        = user.email(),
        password     = UserPassword( data.get( 'user_password' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/validate', methods = [ 'PUT' ] )
def validate():
    # Variables
    data         : dict
    validator    : UserValidator
    responseCode : int
    # Code
    data    = request.json
    validator = UserValidator(
        repository         = UserMysqlRepository(),
        volatileRepository = UserCacheMemoryRepository(),
        eventBus           = EventBus(),
    )
    if not __isValidDataToValidate( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = validator.validate(
        email = UserEmail( data.get( 'user_email' ) ),
        code  = UserCode( data.get( 'user_code' ) ),
    )
    return { 'code' : responseCode }, 202

@userPutController.route( '/api/v1/user/renovate/code', methods = [ 'PUT' ] )
def renovateCode():
    # Variables
    data         : dict
    renovator    : UserRenovator
    responseCode : int
    # Code
    data    = request.json
    renovator = UserRenovator(
        repository  = UserCacheMemoryRepository(),
        emailSender = EmailSender(),
    )
    if not __isValidDataToRenovateCode( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renovator.renovateCode(
        toEmail = UserEmail( data.get( 'user_email' ) ),
    )
    return { 'code' : responseCode }, 202