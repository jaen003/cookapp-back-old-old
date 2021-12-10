"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableRenumerator
from src.table.infrastructure  import TableMysqlRepository
from src.table.domain          import TableNumber
from src.shared.domain         import TableId
from src.shared.infrastructure import RabbitMqEventBus
from src.shared.domain         import INCORRECT_DATA
from src.table.domain          import TableDescription
from src.table.application     import TableRewriter
from src.user.infrastructure   import UserTokenManagerAdapter
from src.user.domain           import UserTokenManager
from src.user.domain           import User
from src.shared.domain         import SERVER_ACCESS_DENIED
from app.middleware            import requestHttp

"""
 *
 * Global variables 
 *
"""

tablePutController = Blueprint( 'tablePutController', __name__ )

"""
 *
 * Methods 
 *
"""

@tablePutController.route( '/api/v1/table/renumber', methods = [ 'PUT' ] )
@requestHttp( [ 'tab_id', 'tab_number' ] )
def renumber( data : dict ):
    # Variables
    renumerator     : TableRenumerator
    responseCode    : int
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
    renumerator = TableRenumerator(
        repository = TableMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renumerator.renumber(
        id           = TableId( data.get( 'tab_id' ) ),
        number       = TableNumber( data.get( 'tab_number' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@tablePutController.route( '/api/v1/table/rewrite', methods = [ 'PUT' ] )
@requestHttp( [ 'tab_id', 'tab_description' ] )
def rewrite( data : dict ):
    # Variables
    rewriter        : TableRewriter
    responseCode    : int
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
    rewriter = TableRewriter(
        repository = TableMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = rewriter.rewrite(
        id           = TableId( data.get( 'tab_id' ) ),
        description  = TableDescription( data.get( 'tab_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
