"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductRenamer
from src.product.infrastructure import ProductRepository
from src.product.domain         import ProductName
from src.shared.domain          import ProductId
from src.shared.infrastructure  import EventBus
from src.shared.domain          import INCORRECT_DATA
from src.product.application    import ProductRevalorizer
from src.product.domain         import ProductPrice
from src.product.application    import ProductRewriter
from src.product.domain         import ProductDescription
from src.shared.domain          import SERVER_ACCESS_DENIED
from src.user.infrastructure    import UserTokenManager
from src.user.domain            import User

"""
 *
 * Global variables 
 *
"""

productPutController = Blueprint( 'productPutController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToRename( data : dict ) -> bool:
    if data.get( 'prod_id' ) is None:
        return False
    if data.get( 'prod_name' ) is None:
        return False
    return True

def __isValidDataToRevalue( data : dict ) -> bool:
    if data.get( 'prod_id' ) is None:
        return False
    if data.get( 'prod_price' ) is None:
        return False
    return True

def __isValidDataToRewrite( data : dict ) -> bool:
    if data.get( 'prod_id' ) is None:
        return False
    if data.get( 'prod_description' ) is None:
        return False
    return True

@productPutController.route( '/api/v1/product/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data            : dict
    renamer         : ProductRenamer
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
    renamer = ProductRenamer(
        repository = ProductRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        id           = ProductId( data.get( 'prod_id' ) ),
        name         = ProductName( data.get( 'prod_name' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@productPutController.route( '/api/v1/product/revalue', methods = [ 'PUT' ] )
def revalue():
    # Variables
    data            : dict
    revalorizer     : ProductRevalorizer
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
    data      = request.json
    revalorizer = ProductRevalorizer(
        repository     = ProductRepository(),
        eventBus       = EventBus(),
    )
    if not __isValidDataToRevalue( data ):
        return { 'code' : INCORRECT_DATA }, 202    
    responseCode = revalorizer.revalue(
        id           = ProductId( data.get( 'prod_id' ) ),
        price        = ProductPrice( data.get( 'prod_price' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202

@productPutController.route( '/api/v1/product/rewrite', methods = [ 'PUT' ] )
def rewrite():
    # Variables
    data            : dict
    rewriter        : ProductRewriter
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
    data     = request.json
    rewriter = ProductRewriter(
        repository = ProductRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRewrite( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = rewriter.rewrite(
        id           = ProductId( data.get( 'prod_id' ) ),
        description  = ProductDescription( data.get( 'prod_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202