"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.user.application      import UserDeletor
from src.user.infrastructure   import UserRepository
from src.shared.domain         import UserEmail
from src.shared.domain         import RestaurantId
from src.shared.infrastructure import EventBus

"""
 *
 * Global variables 
 *
"""

userDeleteController = Blueprint( 'userDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@userDeleteController.route( '/api/v1/user/<string:email>', methods = [ 'DELETE' ] )
def delete( email : str ):
    # Variables
    data         : dict
    deletor      : UserDeletor
    responseCode : int
    # Code
    data    = request.json
    deletor = UserDeletor(
        repository = UserRepository(),
        eventBus   = EventBus(),
    )
    responseCode = deletor.delete(
        email        = UserEmail( email ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202
