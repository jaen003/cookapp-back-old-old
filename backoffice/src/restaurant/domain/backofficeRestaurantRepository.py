"""
 *
 * Libraries 
 *
"""

from abc                       import abstractmethod
from .backofficeRestaurant     import Restaurant
from src.shared.domain         import RestaurantId
from abc                       import ABCMeta
from .backofficeRestaurantName import RestaurantName

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
    def insert( self, restaurant : Restaurant ) -> bool:
        pass
    
    @abstractmethod
    def update( self, restaurant : Restaurant ) -> bool:
        pass

    @abstractmethod
    def selectById( self, id : RestaurantId ) -> Restaurant:
        pass

    @abstractmethod
    def selectByName( self, name : RestaurantName ) -> Restaurant:
        pass