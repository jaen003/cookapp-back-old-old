"""
 *
 * Libraries 
 *
"""

from .DomainException     import DomainException
from .DomainExceptionCode import INVALID_USER_EMAIL

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

    def __init__( self, email : str ) -> None:
        super().__init__(
            INVALID_USER_EMAIL,
            'The user email {} is invalid'.format( email ),
        )