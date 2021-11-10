"""
 *
 * Libraries 
 *
"""

from .backofficeTablePostController import tablePostController
from .backofficeTableGetController  import tableGetController

"""
 *
 * Methods
 *
"""

def exposeTableEntryPoints( server ):
    server.register_blueprint( tablePostController )
    server.register_blueprint( tableGetController )