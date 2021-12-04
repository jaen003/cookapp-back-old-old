"""
 *
 * Libraries 
 *
"""

from .DomainEvent import DomainEvent

"""
 *
 * Classes 
 *
"""

class AggregateRoot:

    """
     *
     * Parameters 
     *
    """

    __events : list[ DomainEvent ]

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        self.__events = []
    
    def record( self, event : DomainEvent ) -> None:
        self.__events.append( event )
    
    def pullEvents( self ) -> list[ DomainEvent ]:
        # Variables
        events : list[ DomainEvent ]
        # Code
        events = self.__events
        self.__events = []
        return events


