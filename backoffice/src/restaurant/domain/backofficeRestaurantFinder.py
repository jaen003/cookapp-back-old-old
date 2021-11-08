"""
 *
 * Libraries 
 *
"""

from .backofficeRestaurantNotFoundException import RestaurantNotFoundException
from .backofficeRestaurantRepository        import RestaurantRepository
from src.shared.domain                      import RestaurantId
from .backofficeRestaurant                  import Restaurant

"""
 *
 * Classes
 *
"""

class RestaurantFinder:

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

    def __init__( self, repository : RestaurantRepository ) -> None:
        self.__repository = repository
    
    def findById( self, id : RestaurantId ) -> Restaurant:
        # Variables
        repository : RestaurantRepository
        data       : Restaurant
        # Code
        repository = self.__repository
        data = repository.selectById( id )
        if data is None:
            raise RestaurantNotFoundException( id )
        return data



