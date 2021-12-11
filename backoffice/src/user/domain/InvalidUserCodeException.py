"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_CODE

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

    def __init__( self, code : str ) -> None:
        super().__init__(
            INVALID_USER_CODE,
            'The user code {} is invalid'.format( code ),
        )