"""
 *
 * Libraries 
 *
"""

from src.shared.domain      import DomainException
from src.shared.domain      import INVALID_TABLE_NUMBER
from .backofficeTableNumber import TableNumber

"""
 *
 * Classes 
 *
"""

class InvalidTableNumberException( DomainException ):

    """
     *
     * Methods 
     *
    """

    def __init__( self, number : TableNumber ) -> None:
        super().__init__(
            INVALID_TABLE_NUMBER,
            'The table number {} is invalid'.format( number.value() )
        )