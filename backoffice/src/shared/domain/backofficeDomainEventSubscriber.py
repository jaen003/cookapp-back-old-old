"""
 *
 * Libraries 
 *
"""

from abc                    import abstractmethod
from .backofficeDomainEvent import DomainEvent

"""
 *
 * Classes 
 *
"""

class DomainEventSubscriber:

    """
     *
     * Parameters 
     *
    """

    __queue : str

    """
     *
     * Methods 
     *
    """

    def __init__( self, queue : str ) -> None:
        self.__queue = queue
    
    def subscribedTo( self ) -> str:
        return self.__queue

    @abstractmethod
    def notify( self, domainEvent : DomainEvent ) -> None:
        pass
