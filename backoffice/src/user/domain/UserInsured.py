"""
 *
 * Libraries 
 *
"""

from .UserPassword     import UserPassword
from src.shared.domain import UserEmail
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class UserInsured( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __email    : UserEmail
    __password : UserPassword

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        email    : UserEmail    = None, 
        password : UserPassword = None,
    ) -> None:
        super().__init__( 'user_insured' )
        self.__email    = email
        self.__password = password
    
    def email( self ) -> UserEmail:
        return self.__email
    
    def password( self ) -> UserPassword:
        return self.__password
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'email'      : self.__email.value(),
            'password'   : self.__password.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__email     = UserEmail( body['email'] )
        self.__password  = UserPassword( body['password'] )

