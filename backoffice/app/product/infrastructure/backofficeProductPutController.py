"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductRenamer
from src.product.infrastructure import ProductRepository
from src.product.domain         import ProductName
from src.shared.domain          import ProductId
from src.shared.domain          import RestaurantId
from src.shared.infrastructure  import EventBus
from src.shared.domain          import INCORRECT_DATA

"""
 *
 * Global variables 
 *
"""

productPutController = Blueprint( 'productPutController', __name__ )

"""
 *
 * Methods 
 *
"""

def __isValidDataToRename( data : dict ) -> bool:
    if data.get( 'prod_id' ) is None:
        return False
    if data.get( 'prod_name' ) is None:
        return False
    return True

@productPutController.route( '/api/v1/product/rename', methods = [ 'PUT' ] )
def rename():
    # Variables
    data         : dict
    renamer      : ProductRenamer
    responseCode : int
    # Code
    data    = request.json
    renamer = ProductRenamer(
        repository = ProductRepository(),
        eventBus   = EventBus(),
    )
    if not __isValidDataToRename( data ):
        return { 'code' : INCORRECT_DATA }, 202
    responseCode = renamer.rename(
        id           = ProductId( data.get( 'prod_id' ) ),
        name         = ProductName( data.get( 'prod_name' ) ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202