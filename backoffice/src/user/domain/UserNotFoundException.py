"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import USER_NOT_FOUND
from src.shared.domain import UserEmail

"""
 *
 * Classes 
 *
"""

class UserNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__( 
            USER_NOT_FOUND,
            'The user {} has not been found'.format( email.value() ),
        )