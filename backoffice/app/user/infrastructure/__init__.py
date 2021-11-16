"""
 *
 * Libraries 
 *
"""

from .backofficeUserPostController                        import userPostController
from .backofficeUserDeleteController                      import userDeleteController
from .backofficeUserPutController                         import userPutController
from src.shared.infrastructure                            import EventBus
from src.user.domain                                      import AdministratorCreated
from .backofficeSendValidationEmailOnAdministratorCreated import SendValidationEmailOnAdministratorCreated

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server, eventBus : EventBus ):
    eventBus.subscribe( 
        event      = AdministratorCreated(), 
        subscriber = SendValidationEmailOnAdministratorCreated(),
    )
    server.register_blueprint( userPostController )
    server.register_blueprint( userDeleteController )
    server.register_blueprint( userPutController )