"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException
from src.shared.domain import TABLE_NUMBER_ALREADY_CREATED
from .TableNumber      import TableNumber

"""
 *
 * Classes 
 *
"""

class TableNumberAlreadyCreatedException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, number : TableNumber ) -> None:
        super().__init__( 
            TABLE_NUMBER_ALREADY_CREATED,
            'The table number {} has already been created'.format( number.value() ),
        )