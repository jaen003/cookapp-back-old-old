"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import USER_DISABLED
from src.shared.domain import UserEmail

"""
 *
 * Classes 
 *
"""

class UserDisabledException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__( 
            USER_DISABLED,
            'The user {} is disabled'.format( email.value() ),
        )