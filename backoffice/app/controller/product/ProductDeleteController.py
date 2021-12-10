"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductDeletor
from src.product.infrastructure import ProductMysqlRepository
from src.shared.domain          import ProductId
from src.shared.infrastructure  import RabbitMqEventBus
from src.shared.domain          import SERVER_ACCESS_DENIED
from src.user.infrastructure    import UserTokenManagerAdapter
from src.user.domain            import UserTokenManager
from src.user.domain            import User

"""
 *
 * Global variables 
 *
"""

productDeleteController = Blueprint( 'productDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@productDeleteController.route( '/api/v1/product/<string:id>', methods = [ 'DELETE' ] )
def delete( id : str ):
    # Variables
    deletor         : ProductDeletor
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
    deletor = ProductDeletor(
        repository = ProductMysqlRepository(),
        eventBus   = RabbitMqEventBus(),
    )
    responseCode = deletor.delete(
        id           = ProductId( id ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
