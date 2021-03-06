"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableDeletor
from src.table.infrastructure  import TableRepository
from src.shared.domain         import TableId
from src.shared.infrastructure import EventBus
from src.user.infrastructure   import UserTokenManager
from src.user.domain           import User
from src.shared.domain         import SERVER_ACCESS_DENIED

"""
 *
 * Global variables 
 *
"""

tableDeleteController = Blueprint( 'tableDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@tableDeleteController.route( '/api/v1/table/<string:id>', methods = [ 'DELETE' ] )
def delete( id : str ):
    # Variables
    deletor         : TableDeletor
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
    deletor = TableDeletor(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    responseCode = deletor.delete(
        id           = TableId( id ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
