"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import PRODUCT_NOT_FOUND
from src.shared.domain import ProductId

"""
 *
 * Classes 
 *
"""

class ProductNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : ProductId ) -> None:
        super().__init__( 
            PRODUCT_NOT_FOUND,
            'The product ' + id.value() + ' has not been found',
        )