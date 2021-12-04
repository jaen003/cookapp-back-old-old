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

class ProductPrice( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __MINIMUN_PRICE = 1

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
    
    def isValid( self ) -> bool:
        if self.isLessThan( self.__MINIMUN_PRICE ):
            return False
        return True