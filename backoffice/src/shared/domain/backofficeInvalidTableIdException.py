"""
 *
 * Libraries 
 *
"""

from .backofficeDomainException    import DomainException
from .backofficeDomainResponseCode import INVALID_TABLE_ID
from .backofficeTableId            import TableId

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