"""
 *
 * Libraries 
 *
"""

from .UserPostController   import userPostController
from .UserDeleteController import userDeleteController
from .UserPutController    import userPutController
from .UserGetController    import userGetController

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server ):
    server.register_blueprint( userPostController )
    server.register_blueprint( userDeleteController )
    server.register_blueprint( userPutController )
    server.register_blueprint( userGetController )