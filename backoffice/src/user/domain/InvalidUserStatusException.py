"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_STATUS

"""
 *
 * Classes 
 *
"""

class InvalidUserStatusException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, status : int ) -> None:
        super().__init__( 
            INVALID_USER_STATUS,
            'The user status {} is invalid'.format( status )
        )