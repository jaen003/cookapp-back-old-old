"""
 *
 * Libraries 
 *
"""

from .TablePostController   import tablePostController
from .TableGetController    import tableGetController
from .TableDeleteController import tableDeleteController
from .TablePutController    import tablePutController

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