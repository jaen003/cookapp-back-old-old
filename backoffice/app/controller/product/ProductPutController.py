"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductRenamer
from src.product.infrastructure import ProductMysqlRepository
from src.product.domain         import ProductName
from src.shared.domain          import ProductId
from src.shared.infrastructure  import RabbitMqEventBus
from src.shared.domain          import INCORRECT_REQUEST_DATA
from src.product.application    import ProductRevalorizer
from src.product.domain         import ProductPrice
from src.product.application    import ProductRewriter
from src.product.domain         import ProductDescription
from src.shared.domain          import SERVER_ACCESS_DENIED
from src.user.infrastructure    import UserTokenManagerAdapter
from src.user.domain            import UserTokenManager
from src.user.domain            import User
from app.middleware             import requestHttp
from src.shared.domain          import DomainException
from src.shared.domain          import SUCCESSFUL_REQUEST

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

@productPutController.route( '/api/v1/product/rename', methods = [ 'PUT' ] )
@requestHttp( [ 'prod_id', 'prod_name' ] )
def rename( data : dict ):
    # Variables
    renamer         : ProductRenamer
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
    renamer = ProductRenamer(
        repository = ProductMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        renamer.rename(
            id           = ProductId( data.get( 'prod_id' ) ),
            name         = ProductName( data.get( 'prod_name' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@productPutController.route( '/api/v1/product/revalue', methods = [ 'PUT' ] )
@requestHttp( [ 'prod_id', 'prod_price' ] )
def revalue( data : dict ):
    # Variables
    revalorizer     : ProductRevalorizer
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
    revalorizer = ProductRevalorizer(
        repository = ProductMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        revalorizer.revalue(
            id           = ProductId( data.get( 'prod_id' ) ),
            price        = ProductPrice( data.get( 'prod_price' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202

@productPutController.route( '/api/v1/product/rewrite', methods = [ 'PUT' ] )
@requestHttp( [ 'prod_id', 'prod_description' ] )
def rewrite( data : dict ):
    # Variables
    rewriter        : ProductRewriter
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
    rewriter = ProductRewriter(
        repository = ProductMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        rewriter.rewrite(
            id           = ProductId( data.get( 'prod_id' ) ),
            description  = ProductDescription( data.get( 'prod_description' ) ),
            restaurantId = user.restaurantId(),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202