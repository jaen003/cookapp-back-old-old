"""
 *
 * Libraries 
 *
"""

import os
from src.user.domain      import UserCode
from src.shared.domain    import UserEmail
from src.user.domain      import UserRepository
from src.user.domain      import User
from src.user.domain      import UserFinder
from jinja2               import Environment
from jinja2               import FileSystemLoader
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart
from src.shared.domain    import EmailSender
from src.shared.domain    import ServerInternalErrorException
from src.user.domain      import UserNotFoundException

"""
 *
 * Classes 
 *
"""

class UserRenovator:

    """
     *
     * Parameters 
     *
    """
 
    __repository  : UserRepository
    __env         : Environment
    __emailSender : EmailSender

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository  : UserRepository,
        emailSender : EmailSender,
    ) -> None:
        self.__repository  = repository
        self.__emailSender = emailSender
        self.__env         = Environment( loader = FileSystemLoader( '/src/app/templates' ) )

    def renovateCode( 
        self, 
        toEmail : UserEmail,
    ) -> None:
        # Variables
        user        : User
        repository  : UserRepository
        finder      : UserFinder
        env         : Environment
        fromEmail   : str
        subject     : str
        emailSender : EmailSender
        code        : UserCode
        # Code
        repository = self.__repository
        finder     = UserFinder( repository )
        user       = finder.findByEmail( toEmail )
        if user is None:
            raise UserNotFoundException( toEmail )
        code = UserCode.short()
        user.renovateCode( code )
        if not repository.update( user ):
            raise ServerInternalErrorException()
        env         = self.__env
        emailSender = self.__emailSender
        template    = env.get_template( 'validationEmail.html' )
        emailBody   = template.render( data = {
            'name' : user.name().value(),
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
