"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from flask                      import request
from src.product.application    import ProductDeletor
from src.product.infrastructure import ProductRepository
from src.shared.domain          import ProductId
from src.shared.domain          import RestaurantId
from src.shared.infrastructure  import EventBus

"""
 *
 * Global variables 
 *
"""

productDeleteController = Blueprint( 'productDeleteController', __name__ )

"""
 *
 * Methods 
 *
"""

@productDeleteController.route( '/api/v1/product/<string:id>', methods = [ 'DELETE' ] )
def delete( id : str ):
    # Variables
    data         : dict
    deletor      : ProductDeletor
    responseCode : int
    # Code
    data    = request.json
    deletor = ProductDeletor(
        repository = ProductRepository(),
        eventBus   = EventBus(),
    )
    responseCode = deletor.delete(
        id           = ProductId( id ),
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode }, 202
