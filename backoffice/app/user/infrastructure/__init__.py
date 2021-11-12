"""
 *
 * Libraries 
 *
"""

from .backofficeUserPostController import userPostController

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server ):
    server.register_blueprint( userPostController )