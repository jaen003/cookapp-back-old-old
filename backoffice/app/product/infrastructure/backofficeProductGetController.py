"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductSearcher
from src.product.infrastructure import ProductRepository
from src.product.domain         import ProductName
from src.shared.domain          import SERVER_ACCESS_DENIED
from src.user.infrastructure    import UserTokenManager
from src.user.domain            import User

"""
 *
 * Global variables 
 *
"""

productGetController = Blueprint( 'productGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@productGetController.route( '/api/v1/product/name/<string:name>', methods = [ 'GET' ] )
def searchAllByNameAndRestaurant( name ):
    # Variables
    responseCode    : int
    products        : list
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
    searcher = ProductSearcher( 
        repository = ProductRepository(),
    )
    products, responseCode = searcher.searchAllByNameAndRestaurant(
        restaurantId = user.restaurantId(),
        name         = ProductName( name ),
    )
    return { 'code' : responseCode, 'data' : products }, 202

@productGetController.route( '/api/v1/product', methods = [ 'GET' ] )
def findAllByRestaurant():
    # Variables
    responseCode    : int
    products        : list
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
    searcher = ProductSearcher( 
        repository = ProductRepository(),
    )
    products, responseCode = searcher.searchAllByRestaurant(
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode, 'data' : products }, 202
