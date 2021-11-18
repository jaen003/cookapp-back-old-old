"""
 *
 * Libraries 
 *
"""

from flask                         import Flask
from app.product.infrastructure    import exposeProductEntryPoints
from app.table.infrastructure      import exposeTableEntryPoints
from app.user.infrastructure       import exposeUserEntryPoints
from app.restaurant.infrastructure import exposeRestaurantEntryPoints
from src.shared.infrastructure     import EventBus

"""
 *
 * Global variables 
 *
"""

server = Flask( __name__ )

"""
 *
 * Methods 
 *
"""

def exposeEntryPoints() -> None:
    # Variables
    eventBus : EventBus
    # Code
    eventBus = EventBus()
    exposeProductEntryPoints( server )
    exposeTableEntryPoints( server )
    exposeUserEntryPoints( server, eventBus )
    exposeRestaurantEntryPoints( server )

def main() -> None:
    exposeEntryPoints()
    server.run( debug = False, host = '0.0.0.0' )

main() # call the main method