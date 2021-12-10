"""
 *
 * Libraries 
 *
"""

from flask                         import Blueprint
from flask                         import request
from src.table.application         import TableCreator
from src.table.infrastructure      import TableMysqlRepository
from src.table.domain              import TableNumber
from src.table.domain              import TableDescription
from src.shared.domain             import TableId
from src.restaurant.infrastructure import RestaurantMysqlRepository
from src.shared.infrastructure     import RabbitMqEventBus
from src.shared.domain             import INCORRECT_DATA
from src.shared.domain             import SERVER_ACCESS_DENIED
from src.user.infrastructure       import UserTokenManagerAdapter
from src.user.domain               import UserTokenManager
from src.user.domain               import User
from app.middleware                import requestHttp

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

@tablePostController.route( '/api/v1/table', methods = [ 'POST' ] )
@requestHttp( [ 'tab_id', 'tab_number' ] )
def create( data : dict ):
    # Variables
    creator         : TableCreator
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
    creator = TableCreator(
        repository           = TableMysqlRepository(),
        restaurantRepository = RestaurantMysqlRepository(),
        eventBus             = RabbitMqEventBus(),
    )
    if not data:
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = creator.create(
        id           = TableId( data.get( 'tab_id' ) ),
        number       = TableNumber( data.get( 'tab_number' ) ),
        description  = TableDescription( data.get( 'tab_description' ) ),
        restaurantId = user.restaurantId(),
    )
    return { 'code' : responseCode }, 202
