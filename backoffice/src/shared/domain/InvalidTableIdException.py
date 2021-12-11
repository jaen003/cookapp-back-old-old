"""
 *
 * Libraries 
 *
"""

from .DomainException     import DomainException
from .DomainExceptionCode import INVALID_TABLE_ID

"""
 *
 * Classes 
 *
"""

class InvalidTableIdException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : str ) -> None:
        super().__init__( 
            INVALID_TABLE_ID,
            'The table id {} is invalid'.format( id )
        )