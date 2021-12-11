"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.user.application      import UserDeletor
from src.user.infrastructure   import UserMysqlRepository
from src.shared.domain         import UserEmail
from src.shared.infrastructure import RabbitMqEventBus
from src.shared.domain         import SERVER_ACCESS_DENIED
from src.user.infrastructure   import UserTokenManagerAdapter
from src.user.domain           import UserTokenManager
from src.user.domain           import User
from src.shared.domain         import DomainException
from src.shared.domain         import SUCCESSFUL_REQUEST

"""
 *
 * Global variables 
 *
"""

userDeleteController = Blueprint( 'userDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@userDeleteController.route( '/api/v1/user/<string:email>', methods = [ 'DELETE' ] )
def delete( email : str ):
    # Variables
    deletor         : UserDeletor
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
    deletor = UserDeletor(
        repository = UserMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    try:
        deletor.delete(
            email        = UserEmail( email ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202
