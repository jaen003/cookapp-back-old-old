"""
 *
 * Libraries 
 *
"""

from .backofficeProductPostController import productPostController

"""
 *
 * Methods
 *
"""

def exposeProductEntryPoints( server ):
    server.register_blueprint( productPostController )
