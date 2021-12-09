"""
 *
 * Libraries 
 *
"""

from .DomainException    import DomainException
from .DomainExceptionCode import INVALID_TABLE_ID
from .TableId            import TableId

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

    def __init__( self, id : TableId ) -> None:
        super().__init__( 
            INVALID_TABLE_ID,
            'The table id {} is invalid'.format( id.value() )
        )