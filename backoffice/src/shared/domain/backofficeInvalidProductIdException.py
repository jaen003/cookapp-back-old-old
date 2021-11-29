"""
 *
 * Libraries 
 *
"""

from .backofficeDomainException    import DomainException
from .backofficeDomainResponseCode import INVALID_PRODUCT_ID
from .backofficeProductId          import ProductId

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

    def __init__( self, id : ProductId ) -> None:
        super().__init__( 
            INVALID_PRODUCT_ID,
            'The product id {} is invalid'.format( id.value() )
        )