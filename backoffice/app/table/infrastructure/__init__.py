"""
 *
 * Libraries 
 *
"""

from .backofficeTablePostController   import tablePostController
from .backofficeTableGetController    import tableGetController
from .backofficeTableDeleteController import tableDeleteController
from .backofficeTablePutController    import tablePutController

"""
 *
 * Methods
 *
"""

def exposeTableEntryPoints( server ):
    server.register_blueprint( tablePostController )
    server.register_blueprint( tableGetController )
    server.register_blueprint( tableDeleteController )
    server.register_blueprint( tablePutController )