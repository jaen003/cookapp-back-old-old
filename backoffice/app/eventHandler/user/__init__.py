"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import EventBus
from src.user.domain              import AdministratorCreated
from .AdministratorCreatedHandler import sendValidationEmail
from .EmployeeCreatedHandler      import sendWelcomeEmail
from src.user.domain              import EmployeeCreated

"""
 *
 * Methods
 *
"""

def suscribeToUserEvents( eventBus : EventBus ):
    eventBus.subscribe( 
        event      = AdministratorCreated(), 
        subscriber = sendValidationEmail,
    )
    eventBus.subscribe( 
        event      = EmployeeCreated(), 
        subscriber = sendWelcomeEmail,
    )