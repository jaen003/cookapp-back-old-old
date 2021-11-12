"""
 *
 * Libraries 
 *
"""

from .backofficeUserName     import UserName
from .backofficeUserPassword import UserPassword
from src.shared.domain       import UserEmail
from src.shared.domain       import RestaurantId
from src.shared.domain       import DomainEvent

"""
 *
 * Classes 
 *
"""

class AdministratorCreated( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __email        : UserEmail
    __name         : UserName
    __password     : UserPassword
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        email        : UserEmail, 
        name         : UserName,
        password     : UserPassword,
        restaurantId : RestaurantId,
    ) -> None:
        super().__init__( 'administrator_created' )
        self.__email        = email
        self.__name         = name
        self.__password     = password
        self.__restaurantId = restaurantId
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'         : self.uuid(),
            'occurredOn'   : str( self.occurredOn() ),
            'email'        : self.__email.value(),
            'name'         : self.__name.value(),
            'password'     : self.__password.value(),
            'restaurantId' : self.__restaurantId.value(),
        }
        return body
    
    def email( self ) -> UserEmail:
        return self.__email
    
    def name( self ) -> UserName:
        return self.__name
    
    def password( self ) -> UserPassword:
        return self.__password

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid          = body['uuid']
        self._occurredOn    = int( body['occurredOn'] )
        self.__email        = UserEmail( body['email'] )
        self.__name         = UserName( body['name'] )
        self.__password     = UserPassword( body['password'] )
        self.__restaurantId = RestaurantId( body['restaurantId'] )