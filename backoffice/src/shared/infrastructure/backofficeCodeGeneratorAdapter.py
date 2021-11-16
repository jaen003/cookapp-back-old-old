"""
 *
 * Libraries 
 *
"""

from src.shared.domain import CodeGenerator
from random            import choice

"""
 *
 * Interfaces
 *
"""

class CodeGenerator( CodeGenerator ):

    """
     *
     * Consts 
     *
    """

    __ALLOWED_VALUES = '0123456789'
    __SHORT_SIZE     = 5    

    """
     *
     * Methods 
     *
    """
    
    def generateShortCode( self ) -> str:
        # Variables
        code : str
        # Code
        code = ''
        code = code.join( [ choice( self.__ALLOWED_VALUES ) for i in range( self.__SHORT_SIZE ) ] )
        return code