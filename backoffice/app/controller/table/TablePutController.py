"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableRenumerator
from src.table.infrastructure  import TableRepository
from src.table.domain          import TableNumber
from src.shared.domain         import TableId
from src.shared.infrastructure import EventBus
from src.shared.domain         import INCORRECT_DATA
from src.table.domain          import TableDescription
from src.table.application     import TableRewriter
from src.user.infrastructure   import UserTokenManager
from src.user.domain           import User
from src.shared.domain         import SERVER_ACCESS_DENIED

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

def __isValidDataToRenumber( data : dict ) -> bool:
    if data.get( 'tab_id' ) is None:
        return False
    if data.get( 'tab_number' ) is None:
        return False
    return True

def __isValidDataToRewrite( data : dict ) -> bool:
    if data.get( 'tab_id' ) is None:
        return False
    if data.get( 'tab_description' ) is None:
        return False
    return True

@tablePutController.route( '/api/v1/table/renumber', methods = [ 'PUT' ] )
def renumber():
    # Variables
    data            : dict
    renumerator     : TableRenumerator
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
    data        = request.json
    renumerator = TableRenumerator(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRenumber( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renumerator.renumber(
        id           = TableId( data.get( 'tab_id' ) ),
        number       = TableNumber( data.get( 'tab_number' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@tablePutController.route( '/api/v1/table/rewrite', methods = [ 'PUT' ] )
def rewrite():
    # Variables
    data            : dict
    rewriter        : TableRewriter
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
    data        = request.json
    rewriter = TableRewriter(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRewrite( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = rewriter.rewrite(
        id           = TableId( data.get( 'tab_id' ) ),
        description  = TableDescription( data.get( 'tab_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
