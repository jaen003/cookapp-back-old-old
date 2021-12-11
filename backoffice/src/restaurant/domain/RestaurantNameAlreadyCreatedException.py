"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import RESTAURANT_NAME_ALREADY_CREATED
from .RestaurantName   import RestaurantName

"""
 *
 * Classes 
 *
"""

class RestaurantNameAlreadyCreatedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : RestaurantName ) -> None:
        super().__init__( 
            RESTAURANT_NAME_ALREADY_CREATED,
            'The restaurant name {} has already been created'.format( name.value() )
        )