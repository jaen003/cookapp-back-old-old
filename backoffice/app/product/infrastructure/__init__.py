"""
 *
 * Libraries 
 *
"""

from .backofficeProductPostController   import productPostController
from .backofficeProductDeleteController import productDeleteController

"""
 *
 * Methods
 *
"""

def exposeProductEntryPoints( server ):
    server.register_blueprint( productPostController )
    server.register_blueprint( productDeleteController )
