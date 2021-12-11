"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import USER_BLOCKED
from src.shared.domain import UserEmail

"""
 *
 * Classes 
 *
"""

class UserBlockedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__( 
            USER_BLOCKED,
            'The user {} is blocked'.format( email.value() ),
        )