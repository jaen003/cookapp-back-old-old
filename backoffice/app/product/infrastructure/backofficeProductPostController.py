"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.product.application       import ProductCreator
from src.product.infrastructure    import ProductRepository
from src.product.domain            import ProductName
from src.product.domain            import ProductPrice
from src.product.domain            import ProductDescription
from src.shared.domain             import ProductId
from src.restaurant.infrastructure import RestaurantRepository
from src.shared.infrastructure     import EventBus
from src.shared.domain             import INCORRECT_DATA
from src.shared.domain             import SERVER_ACCESS_DENIED
from src.user.infrastructure       import UserTokenManager
from src.user.domain               import User

"""
 *
 * Global variables 
 *
"""

productPostController = Blueprint( 'productPostController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidData( data : dict ) -> bool:
    if data.get( 'prod_id' ) is None:
        return False
    if data.get( 'prod_name' ) is None:
        return False
    if data.get( 'prod_price' ) is None:
        return False
    if data.get( 'prod_description' ) is None:
        return False
    return True

@productPostController.route( '/api/v1/product', methods = [ 'POST' ] )
def create():
    # Variables
    data            : dict
    creator         : ProductCreator
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
    creator = ProductCreator(
        repository           = ProductRepository(),
        restaurantRepository = RestaurantRepository(),
        eventBus             = EventBus(),
    )
    if not __isValidData( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.create(
        id           = ProductId( data.get( 'prod_id' ) ),
        name         = ProductName( data.get( 'prod_name' ) ),
        price        = ProductPrice( data.get( 'prod_price' ) ),
        description  = ProductDescription( data.get( 'prod_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
