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
from src.shared.domain             import RestaurantId
from src.shared.domain             import INCORRECT_DATA

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
    data         : dict
    renamer      : RestaurantRenamer
    responseCode : int
    # Code
    data    = request.json
    renamer = RestaurantRenamer(
        repository = RestaurantRepository(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        id   = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        name = RestaurantName( data.get( 'rest_name' ) ),
    )
    return { 'code' : responseCode }, 202