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
from src.shared.domain             import RestaurantId
from src.restaurant.infrastructure import RestaurantRepository
from src.shared.infrastructure     import EventBus
from src.shared.domain             import INCORRECT_DATA

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
    data         : dict
    creator      : TableCreator
    responseCode : int
    # Code
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
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202
