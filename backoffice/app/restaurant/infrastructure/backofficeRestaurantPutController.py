"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.restaurant.application    import RestaurantRenamer
from src.restaurant.infrastructure import RestaurantRepository
from src.restaurant.domain         import RestaurantName
from src.shared.domain             import INCORRECT_DATA
from src.shared.domain             import SERVER_ACCESS_DENIED
from src.user.infrastructure       import UserTokenManager
from src.user.domain               import User

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

def __isValidDataToRename( data : dict ) -> bool:
    if data.get( 'rest_name' ) is None:
        return False
    return True

@restaurantPutController.route( '/api/v1/restaurant/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data            : dict
    renamer         : RestaurantRenamer
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
    renamer = RestaurantRenamer(
        repository = RestaurantRepository(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        id   = user.restaurantId(),
        name = RestaurantName( data.get( 'rest_name' ) ),
    )
    return { 'code' : responseCode }, 202