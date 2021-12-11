"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import USER_ALREADY_CREATED
from src.shared.domain import UserEmail

"""
 *
 * Classes 
 *
"""

class UserAlreadyCreatedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__( 
            USER_ALREADY_CREATED,
            'The user {} has already been created'.format( email.value() ),
        )