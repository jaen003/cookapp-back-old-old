"""
 *
 * Libraries 
 *
"""

from .backofficeUserPostController   import userPostController
from .backofficeUserDeleteController import userDeleteController

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server ):
    server.register_blueprint( userPostController )
    server.register_blueprint( userDeleteController )