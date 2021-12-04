"""
 *
 * Libraries 
 *
"""

from .RestaurantNotFoundException     import RestaurantNotFoundException
from .RestaurantRepository            import RestaurantRepository
from src.shared.domain                import RestaurantId
from .Restaurant                      import Restaurant
from .RestaurantName                  import RestaurantName
from .RestaurantNameNotFoundException import RestaurantNameNotFoundException


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
    
    def findByName( self, name : RestaurantName ) -> Restaurant:
        # Variables
        repository : RestaurantRepository
        data       : Restaurant
        # Code
        repository = self.__repository
        data = repository.selectByName( name )
        if data is None:
            raise RestaurantNameNotFoundException( name )
        return data



