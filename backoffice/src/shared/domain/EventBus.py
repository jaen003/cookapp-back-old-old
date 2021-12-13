"""
 *
 * Libraries 
 *
"""

from abc          import abstractmethod
from .DomainEvent import DomainEvent

"""
 *
 * Classes 
 *
"""

class EventBus:

    """
     *
     * Methods 
     *
    """

    @abstractmethod
    def publish( self, events : list[ DomainEvent ] ) -> None:
        pass

    @abstractmethod
    def subscribe( self, eventName : str, subscriber ) -> None:
        pass