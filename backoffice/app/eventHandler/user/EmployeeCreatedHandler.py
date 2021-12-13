"""
 *
 * Libraries 
 *
"""

from src.user.application      import UserSender
from src.user.domain           import EmployeeCreated
from src.shared.infrastructure import SmtpEmailSender

"""
 *
 * Methods 
 *
"""

def sendWelcomeEmail( event : EmployeeCreated ) -> None:
    # Variables
    sender : UserSender
    # Code
    sender = UserSender(
        emailSender = SmtpEmailSender(),
    )
    sender.sendWelcomeEmail( 
        name     = event.name(), 
        toEmail  = event.email(),
        password = event.password(),
    )