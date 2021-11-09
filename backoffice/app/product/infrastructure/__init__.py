"""
 *
 * Libraries 
 *
"""

from .backofficeProductPostController   import productPostController
from .backofficeProductDeleteController import productDeleteController
from .backofficeProductPutController    import productPutController

"""
 *
 * Methods
 *
"""

def exposeProductEntryPoints( server ):
    server.register_blueprint( productPostController )
    server.register_blueprint( productDeleteController )
    server.register_blueprint( productPutController )
