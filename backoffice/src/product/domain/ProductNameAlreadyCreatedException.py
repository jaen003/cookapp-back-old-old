"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import PRODUCT_NAME_ALREADY_CREATED
from .ProductName      import ProductName

"""
 *
 * Classes 
 *
"""

class ProductNameAlreadyCreatedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : ProductName ) -> None:
        super().__init__( 
            PRODUCT_NAME_ALREADY_CREATED,
            'The product name {} has already been created'.format( name.value() )
        )