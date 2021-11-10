"""
 *
 * Libraries 
 *
"""

from .backofficeTablePostController import tablePostController

"""
 *
 * Methods
 *
"""

def exposeTableEntryPoints( server ):
    server.register_blueprint( tablePostController )