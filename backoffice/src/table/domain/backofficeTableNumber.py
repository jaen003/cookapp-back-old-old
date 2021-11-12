"""
 *
 * Libraries 
 *
"""

from src.shared.domain import IntValueObject

"""
 *
 * Classes 
 *
"""

class TableNumber( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __MINIMUN_NUMBER = 1
    __MAXIMUM_NUMBER = 255

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
    
    def isValid( self ) -> bool:
        if self.isLessThan( self.__MINIMUN_NUMBER ) or self.isBiggerThan( self.__MAXIMUM_NUMBER ):
            return False
        return True