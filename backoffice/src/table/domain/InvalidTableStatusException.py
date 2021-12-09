"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_TABLE_STATUS

"""
 *
 * Classes 
 *
"""

class InvalidTableStatusException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, status : int ) -> None:
        super().__init__( 
            INVALID_TABLE_STATUS,
            'The table status {} is invalid'.format( status )
        )