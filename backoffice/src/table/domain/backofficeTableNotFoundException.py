"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import TABLE_NOT_FOUND
from src.shared.domain import TableId

"""
 *
 * Classes 
 *
"""

class TableNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : TableId ) -> None:
        super().__init__( 
            TABLE_NOT_FOUND,
            'The table {} has not been found'.format( id.value() ),
        )