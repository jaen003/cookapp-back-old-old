"""
 *
 * Libraries 
 *
"""

import os
from src.shared.domain import EmailSender
from smtplib           import SMTP

"""
 *
 * Interfaces
 *
"""

class EmailSender( EmailSender ):

    """
     *
     * Methods 
     *
    """
    
    def send( self, to : list[ str ], message : str ) -> None:
        # Variables
        fromEmail     : str
        emailPassword : str
        # Code
        fromEmail     = os.getenv( 'EMAIL' )
        emailPassword = os.getenv( 'EMAIL_PASSWORD' )
        server        = SMTP( 'smtp.gmail.com', 587 )
        server.starttls()
        server.login( fromEmail, emailPassword )
        server.sendmail( fromEmail, to, message )
        server.quit()