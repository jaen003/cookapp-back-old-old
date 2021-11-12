"""
 *
 * Libraries 
 *
"""

from .backofficeDomainException    import DomainException
from .backofficeDomainResponseCode import INVALID_USER_EMAIL
from .backofficeUserEmail          import UserEmail

"""
 *
 * Classes 
 *
"""

class InvalidUserEmailException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : UserEmail ) -> None:
        super().__init__(
            INVALID_USER_EMAIL,
            'The user email {} is invalid'.format( email.value() ),
        )