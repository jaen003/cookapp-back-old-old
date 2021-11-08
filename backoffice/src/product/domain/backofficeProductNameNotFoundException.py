"""
 *
 * Libraries 
 *
"""

from src.shared.domain      import DomainException
from src.shared.domain      import PRODUCT_NAME_NOT_FOUND
from .backofficeProductName import ProductName

"""
 *
 * Classes 
 *
"""

class ProductNameNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : ProductName ) -> None:
        super().__init__( 
            PRODUCT_NAME_NOT_FOUND,
            'The product name {} has not been found'.format( name.value() ),
        )