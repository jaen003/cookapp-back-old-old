"""
 *
 * Libraries 
 *
"""

from .DomainException    import DomainException
from .DomainExceptionCode import INVALID_USER_EMAIL
from .UserEmail          import UserEmail

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