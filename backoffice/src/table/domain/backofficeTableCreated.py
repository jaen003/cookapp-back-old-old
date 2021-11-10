"""
 *
 * Libraries 
 *
"""

from .backofficeTableNumber      import TableNumber
from .backofficeTableDescription import TableDescription
from src.shared.domain           import TableId
from src.shared.domain           import RestaurantId
from src.shared.domain           import DomainEvent

"""
 *
 * Classes 
 *
"""

class TableCreated( DomainEvent ):

    """
     *
     * Parameters 
     *
    """

    __id           : TableId
    __number       : TableNumber
    __decription   : TableDescription
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : TableId, 
        number       : TableNumber,
        description  : TableDescription,
        restaurantId : RestaurantId,
    ) -> None:
        super().__init__( 'table_created' )
        self.__id           = id
        self.__number       = number
        self.__decription   = description
        self.__restaurantId = restaurantId
    
    def body( self ) -> dict:
        # Variables
        body : dict
        # Code
        body = {
            'uuid'         : self.uuid(),
            'occurredOn'   : str( self.occurredOn() ),
            'id'           : self.__id.value(),
            'number'       : self.__number.value(),
            'description'  : self.__decription.value(),
            'restaurantId' : self.__restaurantId.value(),
        }
        return body
    
    def id( self ) -> TableId:
        return self.__id
    
    def number( self ) -> TableNumber:
        return self.__number
    
    def description( self ) -> TableDescription:
        return self.__decription

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId

    def fromPrimitives( self, body : dict ) -> None:
        self._uuid          = body['uuid']
        self._occurredOn    = int( body['occurredOn'] )
        self.__id           = TableId( body['id'] )
        self.__number       = TableName( body['number'] )
        self.__decription   = TableName( body['description'] )
        self.__restaurantId = RestaurantId( body['restaurantId'] )

