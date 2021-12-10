"""
 *
 * Libraries 
 *
"""

from app.controller.product    import exposeProductEntryPoints
from app.controller.table      import exposeTableEntryPoints
from app.controller.user       import exposeUserEntryPoints
from app.controller.restaurant import exposeRestaurantEntryPoints
from src.shared.infrastructure import RabbitMqEventBus
from src.shared.domain         import EventBus

"""
 *
 * Methods
 *
"""

def exposeEntryPoints( server ) -> None:
    # Variables
    eventBus : EventBus
    # Code
    eventBus = RabbitMqEventBus()
    exposeProductEntryPoints( server )
    exposeTableEntryPoints( server )
    exposeUserEntryPoints( server, eventBus )
    exposeRestaurantEntryPoints( server )