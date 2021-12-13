"""
 *
 * Libraries 
 *
"""

from src.user.application      import UserSender
from src.user.domain           import AdministratorCreated
from src.shared.infrastructure import SmtpEmailSender

"""
 *
 * Methods 
 *
"""

def sendValidationEmail( event : AdministratorCreated ) -> None:
    # Variables
    sender : UserSender
    # Code
    sender = UserSender(
        emailSender = SmtpEmailSender(),
    )
    sender.sendValidationEmail( 
        name    = event.name(), 
        toEmail = event.email(),
        code    = event.code(),
    )