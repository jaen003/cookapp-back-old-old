"""
 *
 * Libraries 
 *
"""

from flask                   import Blueprint
from src.user.application    import UserSearcher
from src.user.infrastructure import UserMysqlRepository
from src.shared.domain       import RestaurantId

"""
 *
 * Global variables 
 *
"""

userGetController = Blueprint( 'userGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@userGetController.route( '/api/v1/user', methods = [ 'GET' ] )
def searchAllByRestaurant():
    # Variables
    responseCode : int
    users        : list
    # Code
    searcher = UserSearcher( 
        repository = UserMysqlRepository(),
    )
    users, responseCode = searcher.searchAllByRestaurant(
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode, 'data' : users }, 202
