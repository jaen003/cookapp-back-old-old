"""
 *
 * Libraries 
 *
"""

from src.shared.domain      import DomainException
from src.shared.domain      import TABLE_NUMBER_NOT_FOUND
from .backofficeTableNumber import TableNumber

"""
 *
 * Classes 
 *
"""

class TableNumberNotFoundException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, number : TableNumber ) -> None:
        super().__init__( 
            TABLE_NUMBER_NOT_FOUND,
            'The table number {} has not been found'.format( number.value() ),
        )