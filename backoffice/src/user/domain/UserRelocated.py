"""
 *
 * Libraries 
 *
"""

from src.shared.domain import UserEmail
from .UserRole         import UserRole
from src.shared.domain import DomainEvent

"""
 *
 * Classes 
 *
"""

class UserRelocated( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __email : UserEmail
    __role  : UserRole

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        email : UserEmail = None, 
        role  : UserRole  = None,
    ) -> None:
        super().__init__( 'user_relocated' )
        self.__email = email
        self.__role  = role
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'       : self.uuid(),
            'occurredOn' : str( self.occurredOn() ),
            'email'      : self.__email.value(),
            'role'       : self.__role.value(),
        }
        return body
    
    def email( self ) -> UserEmail:
        return self.__email
    
    def role( self ) -> UserRole:
        return self.__role

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid       = body['uuid']
        self._occurredOn = int( body['occurredOn'] )
        self.__email     = UserEmail( body['email'] )
        self.__role      = UserRole( body['role'] )