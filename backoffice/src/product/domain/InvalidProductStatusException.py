"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_PRODUCT_STATUS

"""
 *
 * Classes 
 *
"""

class InvalidProductStatusException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, status : int ) -> None:
        super().__init__( 
            INVALID_PRODUCT_STATUS,
            'The product status {} is invalid'.format( status )
        )