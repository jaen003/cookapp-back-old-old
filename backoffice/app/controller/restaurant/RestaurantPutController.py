"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.restaurant.application    import RestaurantRenamer
from src.restaurant.infrastructure import RestaurantMysqlRepository
from src.restaurant.domain         import RestaurantName
from src.shared.domain             import INCORRECT_REQUEST_DATA
from src.shared.domain             import SERVER_ACCESS_DENIED
from src.user.infrastructure       import UserTokenManagerAdapter
from src.user.domain               import UserTokenManager
from src.user.domain               import User
from app.middleware                import requestHttp
from src.shared.domain             import DomainException
from src.shared.domain             import SUCCESSFUL_REQUEST

"""
 *
 * Global variables 
 *
"""

restaurantPutController = Blueprint( 'restaurantPutController', __name__ )

"""
 *
 * Methods 
 *
"""

@restaurantPutController.route( '/api/v1/restaurant/rename', methods = [ 'PUT' ] )
@requestHttp( [ 'rest_name' ] )
def rename( data : dict ):
    # Variables
    renamer         : RestaurantRenamer
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
    renamer = RestaurantRenamer(
        repository = RestaurantMysqlRepository(),
    )
    if not data:
        return { 'code' : INCORRECT_REQUEST_DATA }, 202
    try:
        renamer.rename(
            id   = user.restaurantId(),
            name = RestaurantName( data.get( 'rest_name' ) ),
        )
        return { 'code' : SUCCESSFUL_REQUEST }, 202
    except DomainException as exc:
        return { 'code' : exc.code() }, 202