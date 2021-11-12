"""
 *
 * Libraries 
 *
"""

from src.shared.domain      import DomainException
from src.shared.domain      import INVALID_PRODUCT_NAME
from .backofficeProductName import ProductName

"""
 *
 * Classes 
 *
"""

class InvalidProductNameException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : ProductName ) -> None:
        super().__init__( 
            INVALID_PRODUCT_NAME,
            'The product name {} is invalid'.format( name.value() )
        )