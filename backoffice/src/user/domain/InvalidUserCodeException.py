"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_CODE
from .UserCode         import UserCode

"""
 *
 * Classes 
 *
"""

class InvalidUserCodeException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, code : UserCode ) -> None:
        super().__init__(
            INVALID_USER_CODE,
            'The user code {} is invalid'.format( code.value() ),
        )