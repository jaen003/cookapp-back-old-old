"""
 *
 * Libraries 
 *
"""

from .RestaurantPutController import restaurantPutController

"""
 *
 * Methods
 *
"""

def exposeRestaurantEntryPoints( server ):
    server.register_blueprint( restaurantPutController )