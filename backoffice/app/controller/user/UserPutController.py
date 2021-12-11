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
from src.shared.infrastructure import RabbitMqEventBus
from src.shared.domain         import INCORRECT_REQUEST_DATA
from src.user.application      import UserRelocator
from src.user.domain           import UserRole
from src.user.application      import UserAuthenticator
from src.user.domain           import UserPassword
from src.user.application      import UserInsurer
from src.user.application      import UserValidator
from src.user.domain           import UserCode
from src.shared.infrastructure import SmtpEmailSender
from src.user.application      import UserRenovator
from src.shared.domain         import SERVER_ACCESS_DENIED
from src.user.infrastructure   import UserTokenManagerAdapter
from src.user.domain           import UserTokenManager
from src.user.domain           import User
from app.middleware            import requestHttp
from src.shared.domain         import DomainException
from src.shared.domain         import SUCCESSFUL_REQUEST

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

@userPutController.route( '/api/v1/user/rename', methods = [ 'PUT' ] )
@requestHttp( [ 'user_email', 'user_name' ] )
def rename( data : dict ):
    # Variables
    renamer         : UserRenamer
    headers         : dict
    token           : str
    tokenManager    : UserTokenManager
    user            : User
    isAuthenticated : bool
    # Code
    headers         = request.headers
    tokenManager    = UserTokenManagerAdapter()
    isAuthenticated = False
    try:
        token           = headers['Token']
        user            = tokenManager.decodeToken( token )
        isAuthenticated = user.role().isAdministrator()
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    renamer = UserRenamer(
        repository = UserMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        renamer.rename(
            email        = UserEmail( data.get( 'user_email' ) ),
            name         = UserName( data.get( 'user_name' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/autorename', methods = [ 'PUT' ] )
@requestHttp( [ 'user_name' ] )
def autoRename( data : dict ):
    # Variables
    renamer         : UserRenamer
    headers         : dict
    token           : str
    tokenManager    : UserTokenManager
    user            : User
    isAuthenticated : bool
    # Code
    headers         = request.headers
    tokenManager    = UserTokenManagerAdapter()
    isAuthenticated = False
    try:
        token           = headers['Token']
        user            = tokenManager.decodeToken( token )
        isAuthenticated = True
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    renamer = UserRenamer(
        repository = UserMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        renamer.rename(
            email        = user.email(),
            name         = UserName( data.get( 'user_name' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/relocate', methods = [ 'PUT' ] )
@requestHttp( [ 'user_email', 'user_role' ] )
def relocate( data : dict ):
    # Variables
    relocator       : UserRelocator
    headers         : dict
    token           : str
    tokenManager    : UserTokenManager
    user            : User
    isAuthenticated : bool
    # Code
    headers         = request.headers
    tokenManager    = UserTokenManagerAdapter()
    isAuthenticated = False
    try:
        token           = headers['Token']
        user            = tokenManager.decodeToken( token )
        isAuthenticated = user.role().isAdministrator()
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    relocator = UserRelocator(
        repository = UserMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        relocator.relocate(
            email        = UserEmail( data.get( 'user_email' ) ),
            role         = UserRole( data.get( 'user_role' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/login', methods = [ 'PUT' ] )
@requestHttp( [ 'user_email', 'user_password' ] )
def login( data : dict ):
    # Variables
    authenticator : UserAuthenticator
    response      : dict
    # Code
    authenticator = UserAuthenticator(
        repository   = UserMysqlRepository(),
        tokenManager = UserTokenManagerAdapter(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        response = authenticator.authenticate(
            email    = UserEmail( data.get( 'user_email' ) ),
            password = UserPassword( data.get( 'user_password' ) ),
        )
        return { 'code' : SUCCESSFUL_REQUEST, "data" : response }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/logout', methods = [ 'PUT' ] )
def logout():
    # Variables
    token        : str
    tokenManager : UserTokenManager
    # Code
    headers      = request.headers
    tokenManager = UserTokenManagerAdapter()
    try:
        token = headers['Token']
        tokenManager.expireToken( token )
    except:
        pass
    return {}, 204

@userPutController.route( '/api/v1/user/insure', methods = [ 'PUT' ] )
@requestHttp( [ 'user_password' ] )
def insure( data : dict ):
    # Variables
    insurer         : UserInsurer
    headers         : dict
    token           : str
    tokenManager    : UserTokenManager
    user            : User
    isAuthenticated : bool
    # Code
    headers         = request.headers
    tokenManager    = UserTokenManagerAdapter()
    isAuthenticated = False
    try:
        token           = headers['Token']
        user            = tokenManager.decodeToken( token )
        isAuthenticated = True
    except:
        pass
    if not isAuthenticated:
        return { 'code' : SERVER_ACCESS_DENIED }, 202
    insurer = UserInsurer(
        repository = UserMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        insurer.insure(
            email        = user.email(),
            password     = UserPassword( data.get( 'user_password' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/validate', methods = [ 'PUT' ] )
@requestHttp( [ 'user_email', 'user_code' ] )
def validate( data : dict ):
    # Variables
    validator : UserValidator
    # Code
    validator = UserValidator(
        repository         = UserMysqlRepository(),
        volatileRepository = UserCacheMemoryRepository(),
        eventBus           = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        validator.validate(
            email = UserEmail( data.get( 'user_email' ) ),
            code  = UserCode( data.get( 'user_code' ) ),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@userPutController.route( '/api/v1/user/renovate/code', methods = [ 'PUT' ] )
@requestHttp( [ 'user_email' ] )
def renovateCode( data : dict ):
    # Variables
    renovator : UserRenovator
    # Code
    renovator = UserRenovator(
        repository  = UserCacheMemoryRepository(),
        emailSender = SmtpEmailSender(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        renovator.renovateCode(
            toEmail = UserEmail( data.get( 'user_email' ) ),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202