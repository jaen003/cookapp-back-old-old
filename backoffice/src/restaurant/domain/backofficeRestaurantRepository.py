"""
 *
 * Libraries 
 *
"""

from abc                   import abstractmethod
from .backofficeRestaurant import Restaurant
from src.shared.domain     import RestaurantId
from abc                   import ABCMeta

"""
 *
 * Interfaces
 *
"""

class RestaurantRepository( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """

    @abstractmethod
    def selectById( self, id : RestaurantId ) -> Restaurant:
        pass

    @abstractmethod
    def insert( self, restaurant : Restaurant ) -> bool:
        pass
    
    @abstractmethod
    def update( self, restaurant : Restaurant ) -> bool:
        pass