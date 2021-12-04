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

class Logger( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def info( self, message : str ) -> None:
        pass
    
    @abstractmethod
    def fatal( self, message : str ) -> None:
        pass

    @abstractmethod
    def warning( self, message : str ) -> None:
        pass