"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_PRODUCT_NAME

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

    def __init__( self ) -> None:
        super().__init__( 
            INVALID_PRODUCT_NAME,
            'The product name is invalid'
        )