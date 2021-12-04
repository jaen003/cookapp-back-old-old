"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_NAME
from .UserName         import UserName

"""
 *
 * Classes 
 *
"""

class InvalidUserNameException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : UserName ) -> None:
        super().__init__(
            INVALID_USER_NAME,
            'The user name {} is invalid'.format( name.value() ),
        )