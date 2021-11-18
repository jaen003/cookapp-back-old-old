"""
 *
 * Libraries 
 *
"""

from abc                              import abstractmethod
from .backofficeDomainEvent           import DomainEvent
from .backofficeDomainEventSubscriber import DomainEventSubscriber

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
    def subscribe( self, eventName : str, subscriber : DomainEventSubscriber ) -> None:
        pass