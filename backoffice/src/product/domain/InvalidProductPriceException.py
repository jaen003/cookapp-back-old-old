"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_PRODUCT_PRICE

"""
 *
 * Classes 
 *
"""

class InvalidProductPriceException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, price : int ) -> None:
        super().__init__( 
            INVALID_PRODUCT_PRICE,
            'The product price {} is invalid'.format( price )
        )