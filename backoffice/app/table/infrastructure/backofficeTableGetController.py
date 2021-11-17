"""
 *
 * Libraries 
 *
"""

from flask                    import Blueprint
from src.table.application    import TableSearcher
from src.table.infrastructure import TableRepository
from src.shared.domain        import RestaurantId

"""
 *
 * Global variables 
 *
"""

tableGetController = Blueprint( 'tableGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@tableGetController.route( '/api/v1/table', methods = [ 'GET' ] )
def searchAllByRestaurant():
    # Variables
    responseCode : int
    tables       : list
    # Code
    searcher = TableSearcher( 
        repository = TableRepository(),
    )
    tables, responseCode = searcher.searchAllByRestaurant(
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode, 'data' : tables }, 202
