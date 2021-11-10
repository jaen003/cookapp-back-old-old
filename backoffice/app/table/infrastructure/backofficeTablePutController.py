"""
 *
 * Libraries 
 *
"""

from flask                     import Blueprint
from flask                     import request
from src.table.application     import TableRenumerator
from src.table.infrastructure  import TableRepository
from src.table.domain          import TableNumber
from src.shared.domain         import TableId
from src.shared.domain         import RestaurantId
from src.shared.infrastructure import EventBus
from src.shared.domain         import INCORRECT_DATA
from src.table.domain          import TableDescription
from src.table.application     import TableRewriter

"""
 *
 * Global variables 
 *
"""

tablePutController = Blueprint( 'tablePutController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToRenumber( data : dict ) -> bool:
    if data.get( 'tab_id' ) is None:
        return False
    if data.get( 'tab_number' ) is None:
        return False
    return True

def __isValidDataToRewrite( data : dict ) -> bool:
    if data.get( 'tab_id' ) is None:
        return False
    if data.get( 'tab_description' ) is None:
        return False
    return True

@tablePutController.route( '/api/v1/table/renumber', methods = [ 'PUT' ] )
def renumber():
    # Variables
    data         : dict
    renumerator  : TableRenumerator
    responseCode : int
    # Code
    data        = request.json
    renumerator = TableRenumerator(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRenumber( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renumerator.renumber(
        id           = TableId( data.get( 'tab_id' ) ),
        number       = TableNumber( data.get( 'tab_number' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202

@tablePutController.route( '/api/v1/table/rewrite', methods = [ 'PUT' ] )
def rewrite():
    # Variables
    data         : dict
    rewriter     : TableRewriter
    responseCode : int
    # Code
    data        = request.json
    rewriter = TableRewriter(
        repository = TableRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRewrite( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = rewriter.rewrite(
        id           = TableId( data.get( 'tab_id' ) ),
        description  = TableDescription( data.get( 'tab_description' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202
