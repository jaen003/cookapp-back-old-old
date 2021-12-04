"""
 *
 * Libraries 
 *
"""

from .ProductPostController   import productPostController
from .ProductDeleteController import productDeleteController
from .ProductPutController    import productPutController
from .ProductGetController    import productGetController

"""
 *
 * Methods
 *
"""

def exposeProductEntryPoints( server ):
    server.register_blueprint( productPostController )
    server.register_blueprint( productDeleteController )
    server.register_blueprint( productPutController )
    server.register_blueprint( productGetController )
