"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain import RestaurantName
from src.shared.domain     import RestaurantId
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import Restaurant
from src.restaurant.domain import RestaurantFinder
from src.shared.domain     import RestaurantId
from src.restaurant.domain import RestaurantNotFoundException
from src.shared.domain     import ServerInternalErrorException
from src.restaurant.domain import RestaurantNameAlreadyCreatedException

"""
 *
 * Classes 
 *
"""

class RestaurantRenamer:

    """
     *
     * Parameters 
     *
    """
 
    __repository : RestaurantRepository

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository : RestaurantRepository,
    ) -> None:
        self.__repository = repository

    def rename( 
        self, 
        id   : RestaurantId, 
        name : RestaurantName,
    ) -> None:
        # Variables
        restaurant : Restaurant
        repository : RestaurantRepository
        finder     : RestaurantFinder
        # Code
        repository = self.__repository
        finder     = RestaurantFinder( repository )
        restaurant = finder.findByName( name )
        if restaurant is not None:
            raise RestaurantNameAlreadyCreatedException( name )
        restaurant = finder.findById( id )
        if restaurant is None:
            raise RestaurantNotFoundException( id )
        restaurant.rename( name )
        if not repository.update( restaurant ):
            raise ServerInternalErrorException()