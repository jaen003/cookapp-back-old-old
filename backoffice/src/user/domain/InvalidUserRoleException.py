"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INVALID_USER_ROLE

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

    def __init__( self, role : int ) -> None:
        super().__init__(
            INVALID_USER_ROLE,
            'The user role {} is invalid'.format( role ),
        )