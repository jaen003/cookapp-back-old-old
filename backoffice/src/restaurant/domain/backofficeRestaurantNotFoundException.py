"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import RESTAURANT_NOT_FOUND
from src.shared.domain import RestaurantId

"""
 *
 * Classes 
 *
"""

class RestaurantNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : RestaurantId ) -> None:
        super().__init__( 
            RESTAURANT_NOT_FOUND,
            'The restaurant {} has not been found'.format( id.value() )
        )