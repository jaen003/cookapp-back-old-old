"""
 *
 * Libraries 
 *
"""

from src.user.application      import UserSender
from src.shared.domain         import DomainEventSubscriber
from src.user.domain           import AdministratorCreated
from src.shared.infrastructure import EmailSender
from src.user.infrastructure   import UserCacheMemoryRepository

"""
 *
 * Classes 
 *
"""

class SendValidationEmailOnAdministratorCreated( DomainEventSubscriber ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ):
        super().__init__( 'backoffice_administrator_created' )

    def notify( self, event : AdministratorCreated ) -> None:
        # Variables
        sender : UserSender
        # Code
        sender = UserSender(
            emailSender = EmailSender(),
            repository  = UserCacheMemoryRepository(),
        )
        sender.sendValidationEmail( 
            name    = event.name(), 
            toEmail = event.email(),
            code    = event.code(),
        )