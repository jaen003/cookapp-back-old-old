"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain import RestaurantName
from src.shared.domain     import RestaurantId
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import Restaurant
from src.shared.domain     import SUCCESSFUL_REQUEST
from src.shared.domain     import SERVER_INTERNAL_ERROR
from src.shared.domain     import RESTAURANT_ALREADY_CREATED
from src.shared.domain     import DomainException
from src.restaurant.domain import RestaurantFinder
from src.shared.domain     import RestaurantId

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
    ) -> int:
        # Variables
        restaurant : Restaurant
        repository : RestaurantRepository
        finder     : RestaurantFinder
        # Code
        repository = self.__repository
        finder     = RestaurantFinder( repository )
        try:
            try:
                finder.findByName( name )
                return RESTAURANT_ALREADY_CREATED
            except DomainException:
                pass
            restaurant = finder.findById( id )
            restaurant.rename( name )
            if repository.update( restaurant ):
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
