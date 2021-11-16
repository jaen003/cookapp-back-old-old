"""
 *
 * Libraries 
 *
"""

from abc import abstractmethod
from abc import ABCMeta

"""
 *
 * Interfaces
 *
"""

class CodeGenerator( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def generateShortCode( self ) -> str:
        pass