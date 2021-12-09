"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_RESTAURANT_STATUS

"""
 *
 * Classes 
 *
"""

class InvalidRestaurantStatusException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, status : int ) -> None:
        super().__init__( 
            INVALID_RESTAURANT_STATUS,
            'The restaurant status {} is invalid'.format( status )
        )