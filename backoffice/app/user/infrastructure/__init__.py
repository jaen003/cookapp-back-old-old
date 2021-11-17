"""
 *
 * Libraries 
 *
"""

from .backofficeUserPostController              import userPostController
from .backofficeUserDeleteController            import userDeleteController
from .backofficeUserPutController               import userPutController
from src.shared.infrastructure                  import EventBus
from src.user.domain                            import AdministratorCreated
from .backofficeSendEmailOnAdministratorCreated import SendEmailOnAdministratorCreated
from .backofficeSendEmailOnEmployeeCreated      import SendEmailOnEmployeeCreated
from src.user.domain                            import EmployeeCreated

"""
 *
 * Methods
 *
"""

def exposeUserEntryPoints( server, eventBus : EventBus ):
    eventBus.subscribe( 
        event      = AdministratorCreated(), 
        subscriber = SendEmailOnAdministratorCreated(),
    )
    eventBus.subscribe( 
        event      = EmployeeCreated(), 
        subscriber = SendEmailOnEmployeeCreated(),
    )
    server.register_blueprint( userPostController )
    server.register_blueprint( userDeleteController )
    server.register_blueprint( userPutController )