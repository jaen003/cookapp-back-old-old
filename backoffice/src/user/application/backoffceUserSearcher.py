"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRepository
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import RestaurantId

"""
 *
 * Classes 
 *
"""

class UserSearcher:

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

    def searchAllByRestaurant( 
        self,
        restaurantId : RestaurantId,
    ) -> tuple[ list, int ]:
        # Variables
        repository : UserRepository
        users      : list
        # Code
        repository = self.__repository
        users      = repository.selectAllByRestaurant( restaurantId )
        return users, SUCCESSFUL_REQUEST
