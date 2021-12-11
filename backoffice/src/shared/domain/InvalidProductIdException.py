"""
 *
 * Libraries 
 *
"""

from .DomainException     import DomainException
from .DomainExceptionCode import INVALID_PRODUCT_ID

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

    def __init__( self, id : str ) -> None:
        super().__init__( 
            INVALID_PRODUCT_ID,
            'The product id {} is invalid'.format( id )
        )