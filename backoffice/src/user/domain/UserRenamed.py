"""
 *
 * Libraries 
 *
"""

from .UserName         import UserName
from src.shared.domain import UserEmail
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class UserRenamed( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __email : UserEmail
    __name  : UserName

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        email : UserEmail = None, 
        name  : UserName  = None,
    ) -> None:
        super().__init__( 'user_renamed' )
        self.__email = email
        self.__name  = name
    
    def email( self ) -> UserEmail:
        return self.__email
    
    def name( self ) -> UserName:
        return self.__name
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'email'      : self.__email.value(),
            'name'       : self.__name.value(),
        }
        return body

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__email     = UserEmail( body['email'] )
        self.__name      = UserName( body['name'] )

