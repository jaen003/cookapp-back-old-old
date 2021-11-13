"""
 *
 * Libraries 
 *
"""

from abc               import abstractmethod
from .backofficeUser   import User
from src.shared.domain import UserEmail
from abc               import ABCMeta
from src.shared.domain import RestaurantId

"""
 *
 * Interfaces
 *
"""

class UserRepository( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def insert( self, user : User ) -> bool:
        pass
    
    @abstractmethod
    def update( self, user : User ) -> bool:
        pass

    @abstractmethod
    def selectByEmailAndRestaurant( self, email : UserEmail, restaurantId : RestaurantId ) -> User:
        pass

    @abstractmethod
    def selectByEmail( self, email : UserEmail ) -> User:
        pass