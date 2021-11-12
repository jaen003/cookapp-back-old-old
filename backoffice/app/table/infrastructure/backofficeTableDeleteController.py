"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableDeletor
from src.table.infrastructure  import TableRepository
from src.shared.domain         import TableId
from src.shared.domain         import RestaurantId
from src.shared.infrastructure import EventBus

"""
 *
 * Global variables 
 *
"""

tableDeleteController = Blueprint( 'tableDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@tableDeleteController.route( '/api/v1/table/<string:id>', methods = [ 'DELETE' ] )
def delete( id : str ):
    # Variables
    data         : dict
    deletor      : TableDeletor
    responseCode : int
    # Code
    data    = request.json
    deletor = TableDeletor(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    responseCode = deletor.delete(
        id           = TableId( id ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202
