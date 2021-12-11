"""
 *
 * Libraries 
 *
"""

from .DomainException     import DomainException
from .DomainExceptionCode import SERVER_INTERNAL_ERROR

"""
 *
 * Classes 
 *
"""

class ServerInternalErrorException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        super().__init__( 
            SERVER_INTERNAL_ERROR,
            'Internal server error occurred while the request was being processed'
        )
