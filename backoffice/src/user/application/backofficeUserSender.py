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
from src.user.domain      import UserCode
from src.user.domain      import UserPassword

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

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        emailSender : EmailSender,
    ) -> None:
        self.__emailSender = emailSender
        self.__env         = Environment( loader = FileSystemLoader( '/src/app/templates' ) )

    def sendValidationEmail( 
        self, 
        toEmail : UserEmail,
        name    : UserName,
        code    : UserCode,
    ) -> int:
        # Variables
        env         : Environment
        fromEmail   : str
        subject     : str
        emailSender : EmailSender
        # Code
        env         = self.__env
        emailSender = self.__emailSender
        template    = env.get_template( 'validationEmail.html' )
        emailBody   = template.render( data = {
            'name' : name.value(),
            'code' : code.value(),
        } )
        subject            = 'Verify your new Cookapp account.'
        fromEmail          = os.getenv( 'EMAIL' )
        message            = MIMEMultipart()
        message['Subject'] = subject
        message['From']    = fromEmail
        message['To']      = toEmail.value()
        message.attach( MIMEText( emailBody, 'html' ) )
        emailSender.send( toEmail.value(), message.as_string() )
    
    def sendWelcomeEmail(
        self, 
        toEmail  : UserEmail,
        name     : UserName,
        password : UserPassword,
    ) -> int:
        # Variables
        env         : Environment
        fromEmail   : str
        subject     : str
        emailSender : EmailSender
        # Code
        env         = self.__env
        emailSender = self.__emailSender
        template    = env.get_template( 'welcomeEmail.html' )
        emailBody   = template.render( data = {
            'name'     : name.value(),
            'user'     : toEmail.value(),
            'password' : password.value(),
        } )
        subject            = '¡Welcome to your Cookapp account!'
        fromEmail          = os.getenv( 'EMAIL' )
        message            = MIMEMultipart()
        message['Subject'] = subject
        message['From']    = fromEmail
        message['To']      = toEmail.value()
        message.attach( MIMEText( emailBody, 'html' ) )
        emailSender.send( toEmail.value(), message.as_string() )
