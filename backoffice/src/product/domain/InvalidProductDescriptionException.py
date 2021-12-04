"""
 *
 * Libraries 
 *
"""

from src.shared.domain   import DomainException
from src.shared.domain   import INVALID_PRODUCT_DESCRIPTION
from .ProductDescription import ProductDescription

"""
 *
 * Classes 
 *
"""

class InvalidProductDescriptionException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, description : ProductDescription ) -> None:
        super().__init__( 
            INVALID_PRODUCT_DESCRIPTION,
            'The product description {} is invalid'.format( description.value() )
        )