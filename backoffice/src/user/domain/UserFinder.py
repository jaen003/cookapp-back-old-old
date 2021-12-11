"""
 *
 * Libraries 
 *
"""

from .UserRepository   import UserRepository
from src.shared.domain import UserEmail
from src.shared.domain import RestaurantId
from .User             import User

"""
 *
 * Classes
 *
"""

class UserFinder:

    """
     *
     * Parameters 
     *
    """

    __repository : UserRepository

    """
     *
     * Methods 
     *
    """

    def __init__( self, repository : UserRepository ) -> None:
        self.__repository = repository
    
    def findByEmailAndRestaurant( self, email : UserEmail, restaurantId : RestaurantId ) -> User:
        # Variables
        repository : UserRepository
        data       : User
        # Code
        repository = self.__repository
        data = repository.selectByEmailAndRestaurant( email, restaurantId )
        return data
    
    def findByEmail( self, email : UserEmail ) -> User:
        # Variables
        repository : UserRepository
        data       : User
        # Code
        repository = self.__repository
        data = repository.selectByEmail( email )
        return data