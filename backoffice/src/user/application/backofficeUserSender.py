"""
 *
 * Libraries 
 *
"""

import os
from src.shared.domain    import UserEmail
from src.user.domain      import UserName
from jinja2               import Environment
from jinja2               import FileSystemLoader
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart
from src.shared.domain    import EmailSender
from src.user.domain      import UserRepository
from src.user.domain      import User

"""
 *
 * Classes 
 *
"""

class UserSender:

    """
     *
     * Parameters 
     *
    """
 
    __env         : Environment
    __emailSender : EmailSender
    __repository  : UserRepository

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        emailSender : EmailSender,
        repository  : UserRepository,
    ) -> None:
        self.__emailSender = emailSender
        self.__repository  = repository
        self.__env         = Environment( loader = FileSystemLoader( '/src/app/templates' ) )

    def sendValidationEmail( 
        self, 
        toEmail : UserEmail,
        name    : UserName,
        code    : str,
    ) -> int:
        # Variables
        env         : Environment
        fromEmail   : str
        subject     : str
        emailSender : EmailSender
        repository  : UserRepository
        user        : User
        # Code
        env         = self.__env
        emailSender = self.__emailSender
        repository  = self.__repository
        template    = env.get_template( 'emailValidation.html' )
        emailBody   = template.render( data = {
            'name' : name.value(),
            'code' : code,
        } )
        subject            = 'Email verification.'
        fromEmail          = os.getenv( 'EMAIL' )
        message            = MIMEMultipart()
        message['Subject'] = subject
        message['From']    = fromEmail
        message['To']      = toEmail.value()
        message.attach( MIMEText( emailBody, 'html' ) )
        emailSender.send( toEmail.value(), message.as_string() )
        user = User( 
            email        = toEmail,
            name         = None,
            password     = None,
            role         = None,
            status       = None,
            restaurantId = None,
            code         = code,
        )
        repository.insert( user )
