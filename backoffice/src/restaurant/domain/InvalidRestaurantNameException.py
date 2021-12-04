"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_RESTAURANT_NAME
from .RestaurantName   import RestaurantName

"""
 *
 * Classes 
 *
"""

class InvalidRestaurantNameException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : RestaurantName ) -> None:
        super().__init__( 
            INVALID_RESTAURANT_NAME,
            'The restaurant name {} is invalid'.format( name.value() )
        )