"""
 *
 * Libraries 
 *
"""

from .backofficeDomainException    import DomainException
from .backofficeDomainResponseCode import INVALID_PRODUCT_ID

"""
 *
 * Classes 
 *
"""

class InvalidProductIdException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        super().__init__( 
            INVALID_PRODUCT_ID,
            'The product id is invalid'
        )