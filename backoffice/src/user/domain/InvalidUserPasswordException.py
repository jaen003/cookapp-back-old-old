"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_PASSWORD

"""
 *
 * Classes 
 *
"""

class InvalidUserPasswordException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, password : str ) -> None:
        super().__init__(
            INVALID_USER_PASSWORD,
            'The user password {} is invalid'.format( password ),
        )