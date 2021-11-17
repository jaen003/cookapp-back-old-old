"""
 *
 * Libraries 
 *
"""

from src.shared.domain         import DomainException
from src.shared.domain         import RESTAURANT_NAME_NOT_FOUND
from .backofficeRestaurantName import RestaurantName

"""
 *
 * Classes 
 *
"""

class RestaurantNameNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : RestaurantName ) -> None:
        super().__init__( 
            RESTAURANT_NAME_NOT_FOUND,
            'The restaurant name {} has not been found'.format( name.value() ),
        )