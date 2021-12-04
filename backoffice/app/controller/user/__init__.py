"""
 *
 * Libraries 
 *
"""

from .UserPostController              import userPostController
from .UserDeleteController            import userDeleteController
from .UserPutController               import userPutController
from .UserGetController               import userGetController
from src.shared.infrastructure        import EventBus
from src.user.domain                  import AdministratorCreated
from .SendEmailOnAdministratorCreated import SendEmailOnAdministratorCreated
from .SendEmailOnEmployeeCreated      import SendEmailOnEmployeeCreated
from src.user.domain                  import EmployeeCreated

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
    server.register_blueprint( userGetController )