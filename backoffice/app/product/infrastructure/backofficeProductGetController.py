"""
 *
 * Libraries 
 *
"""

from flask                      import Blueprint
from src.product.application    import ProductReader
from src.product.infrastructure import ProductRepository
from src.product.domain         import ProductName
from src.shared.domain          import RestaurantId

"""
 *
 * Global variables 
 *
"""

productGetController = Blueprint( 'productGetController', __name__ )

"""
 *
 * Methods 
 *
"""

@productGetController.route( '/api/v1/product/name/<string:name>', methods = [ 'GET' ] )
def findAllByNameAndRestaurant( name ):
    # Variables
    responseCode : int
    products     : list
    # Code
    reader = ProductReader( 
        repository = ProductRepository(),
    )
    products, responseCode = reader.findAllByNameAndRestaurant(
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        name         = ProductName( name ),
    )
    return { 'code' : responseCode, 'data' : products }, 202

@productGetController.route( '/api/v1/product', methods = [ 'GET' ] )
def findAllByRestaurant():
    # Variables
    responseCode : int
    products     : list
    # Code
    reader = ProductReader( 
        repository = ProductRepository(),
    )
    products, responseCode = reader.findAllByRestaurant(
        restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
    )
    return { 'code' : responseCode, 'data' : products }, 202
