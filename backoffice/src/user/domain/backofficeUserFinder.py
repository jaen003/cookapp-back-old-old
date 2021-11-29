"""
 *
 * Libraries 
 *
"""

from .backofficeUserNotFoundException import UserNotFoundException
from .backofficeUserRepository        import UserRepository
from src.shared.domain                import UserEmail
from src.shared.domain                import RestaurantId
from .backofficeUser                  import User

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
        if data is None:
            raise UserNotFoundException( email )
        return data
    
    def findByEmail( self, email : UserEmail ) -> User:
        # Variables
        repository : UserRepository
        data       : User
        # Code
        repository = self.__repository
        data = repository.selectByEmail( email )
        if data is None:
            raise UserNotFoundException( email )
        return data