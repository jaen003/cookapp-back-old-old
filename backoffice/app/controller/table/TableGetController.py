"""
 *
 * Libraries 
 *
"""

from flask                    import Blueprint
from flask                    import request
from src.table.application    import TableSearcher
from src.table.infrastructure import TableMysqlRepository
from src.user.infrastructure  import UserTokenManagerAdapter
from src.user.domain          import UserTokenManager
from src.user.domain          import User
from src.shared.domain        import SERVER_ACCESS_DENIED
from src.shared.domain        import SUCCESSFUL_REQUEST

"""
 *
 * Global variables 
 *
"""

tableGetController = Blueprint( 'tableGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@tableGetController.route( '/api/v1/table', methods = [ 'GET' ] )
def searchAllByRestaurant():
    # Variables
    tables          : list
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
    searcher = TableSearcher( 
        repository = TableMysqlRepository(),
    )
    tables = searcher.searchAllByRestaurant(
        restaurantId = user.restaurantId(),
    )
    return { 'code' : SUCCESSFUL_REQUEST, 'data' : tables }, 202
