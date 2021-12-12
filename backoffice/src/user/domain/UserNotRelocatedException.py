"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import USER_NOT_RELOCATED
from src.shared.domain import UserEmail

"""
 *
 * Classes 
 *
"""

class UserNotRelocatedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__( 
            USER_NOT_RELOCATED,
            'The user {} was not relocated'.format( email.value() ),
        )