"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.user.application      import UserRenamer
from src.user.infrastructure   import UserRepository
from src.user.domain           import UserName
from src.shared.domain         import UserEmail
from src.shared.domain         import RestaurantId
from src.shared.infrastructure import EventBus
from src.shared.domain         import INCORRECT_DATA

"""
 *
 * Global variables 
 *
"""

userPutController = Blueprint( 'userPutController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToRename( data : dict ) -> bool:
    if data.get( 'user_email' ) is None:
        return False
    if data.get( 'user_name' ) is None:
        return False
    return True

@userPutController.route( '/api/v1/user/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data         : dict
    renamer      : UserRenamer
    responseCode : int
    # Code
    data    = request.json
    renamer = UserRenamer(
        repository = UserRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        email        = UserEmail( data.get( 'user_email' ) ),
        name         = UserName( data.get( 'user_name' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202