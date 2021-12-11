"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableDeletor
from src.table.infrastructure  import TableMysqlRepository
from src.shared.domain         import TableId
from src.shared.infrastructure import RabbitMqEventBus
from src.user.infrastructure   import UserTokenManagerAdapter
from src.user.domain           import UserTokenManager
from src.user.domain           import User
from src.shared.domain         import SERVER_ACCESS_DENIED
from src.shared.domain         import DomainException
from src.shared.domain         import SUCCESSFUL_REQUEST

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
    deletor = TableDeletor(
        repository = TableMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    try:
        deletor.delete(
            id           = TableId( id ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202
