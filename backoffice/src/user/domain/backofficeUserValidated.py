"""
 *
 * Libraries 
 *
"""

from src.shared.domain import UserEmail
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class UserValidated( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __email : UserEmail

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        email : UserEmail,
    ) -> None:
        super().__init__( 'user_validated' )
        self.__email = email
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'email'      : self.__email.value(),
        }
        return body
    
    def email( self ) -> UserEmail:
        return self.__email

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__email     = UserEmail( body['email'] )

