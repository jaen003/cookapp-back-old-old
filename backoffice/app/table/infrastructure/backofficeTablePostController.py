"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.table.application         import TableCreator
from src.table.infrastructure      import TableRepository
from src.table.domain              import TableNumber
from src.table.domain              import TableDescription
from src.shared.domain             import TableId
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

tablePostController = Blueprint( 'tablePostController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidData( data : dict ) -> bool:
    if data.get( 'tab_id' ) is None:
        return False
    if data.get( 'tab_number' ) is None:
        return False
    return True

@tablePostController.route( '/api/v1/table', methods = [ 'POST' ] )
def create():
    # Variables
    data            : dict
    creator         : TableCreator
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
    creator = TableCreator(
        repository           = TableRepository(),
        restaurantRepository = RestaurantRepository(),
        eventBus             = EventBus(),
    )
    if not __isValidData( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.create(
        id           = TableId( data.get( 'tab_id' ) ),
        number       = TableNumber( data.get( 'tab_number' ) ),
        description  = TableDescription( data.get( 'tab_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
