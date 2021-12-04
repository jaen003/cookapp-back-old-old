"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_ROLE
from .UserRole         import UserRole

"""
 *
 * Classes 
 *
"""

class InvalidUserRoleException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, role : UserRole ) -> None:
        super().__init__(
            INVALID_USER_ROLE,
            'The user role {} is invalid'.format( role.value() ),
        )