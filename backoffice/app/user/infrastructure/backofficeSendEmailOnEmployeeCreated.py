"""
 *
 * Libraries 
 *
"""

from src.user.application      import UserSender
from src.shared.domain         import DomainEventSubscriber
from src.user.domain           import EmployeeCreated
from src.shared.infrastructure import EmailSender

"""
 *
 * Classes 
 *
"""

class SendEmailOnEmployeeCreated( DomainEventSubscriber ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ):
        super().__init__( 'backoffice_employee_created' )

    def notify( self, event : EmployeeCreated ) -> None:
        # Variables
        sender : UserSender
        # Code
        sender = UserSender(
            emailSender = EmailSender(),
        )
        sender.sendWelcomeEmail( 
            name     = event.name(), 
            toEmail  = event.email(),
            password = event.password(),
        )