"""
 *
 * Libraries 
 *
"""

from abc                        import abstractmethod
from datetime                   import datetime
from .backofficeUuidValueObject import UuidValueObject

"""
 *
 * Classes 
 *
"""

class DomainEvent:

    """
     *
     * Parameters 
     *
    """

    __topic     : str
    _occurredOn : int
    _uuid       : str

    """
     *
     * Methods 
     *
    """

    def __init__( self, topic : str ) -> None:
        # Variables
        timestamp : int
        # Code
        now              = datetime.now()
        timestamp        = int( datetime.timestamp( now ) )
        self._uuid       = UuidValueObject.random().value()
        self.__topic     = topic
        self._occurredOn = timestamp
    
    def topic( self ) -> str:
        return self.__topic
    
    def occurredOn( self ) -> int:
        return self._occurredOn
    
    def uuid( self ) -> str:
        return self._uuid
    
    @abstractmethod
    def body( self ) -> dict:
        pass

    @abstractmethod
    def fromPrimitives( self, body : dict ) -> None:
        pass
