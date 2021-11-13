"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock         import Mock 
from src.table.domain      import Table
from src.shared.domain     import TableId
from src.table.domain      import TableNumber
from src.table.domain      import TableDescription
from src.shared.domain     import RestaurantId
from src.shared.domain     import DomainException
from src.table.application import TableDeletor

"""
 *
 * Classes 
 *
"""

class TestSuite( unittest.TestCase ):

    """
     *
     * Parameters 
     *
    """

    __table : Table

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__table = Table( 
            TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            TableNumber( 17 ),
            TableDescription( 'Nice place' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testTableDeletedSuccessfully( self ):
        # Variables
        responseCode : int
        deletor      : TableDeletor
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        eventBusMock = Mock()
        deletor = TableDeletor(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = deletor.delete( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testTableNotRemovedBecauseItNotFound( self ):
        # Variables
        responseCode : int
        deletor      : TableDeletor
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        eventBusMock = Mock()
        deletor = TableDeletor(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = deletor.delete( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 135 )
    
    def testTableNotRemovedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        deletor      : TableDeletor
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        repositoryMock.update.return_value = False
        eventBusMock = Mock()
        deletor = TableDeletor(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = deletor.delete( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )