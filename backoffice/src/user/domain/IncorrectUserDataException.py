"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import INCORRECT_USER_DATA

"""
 *
 * Classes 
 *
"""

class IncorrectUserDataException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        super().__init__( 
            INCORRECT_USER_DATA,
            'User data is incorrect'
        )
