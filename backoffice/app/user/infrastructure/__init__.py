"""
 *
 * Libraries 
 *
"""

from .backofficeUserPostController   import userPostController
from .backofficeUserDeleteController import userDeleteController
from .backofficeUserPutController    import userPutController

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server ):
    server.register_blueprint( userPostController )
    server.register_blueprint( userDeleteController )
    server.register_blueprint( userPutController )