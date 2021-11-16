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

class EmailSender( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def send( self, to : list[ str ], message : str ) -> None:
        pass