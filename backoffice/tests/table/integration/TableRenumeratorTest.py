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
from src.table.application import TableRenumerator

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

    def testTableRenumberedSuccessfully( self ):
        # Variables
        responseCode : int
        renumerator  : TableRenumerator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        eventBusMock = Mock()
        renumerator = TableRenumerator(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = renumerator.renumber( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 6 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testTableNotRenumberedBecauseItAlreadyExists( self ):
        # Variables
        responseCode : int
        renumerator  : TableRenumerator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = self.__table
        eventBusMock = Mock()
        renumerator = TableRenumerator(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = renumerator.renumber( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 6 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 137 )
    
    def testTableNotRenumberedBecauseItNotFound( self ):
        # Variables
        responseCode : int
        renumerator  : TableRenumerator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        repositoryMock.selectByIdAndRestaurant.return_value = None
        eventBusMock = Mock()
        renumerator = TableRenumerator(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = renumerator.renumber( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 6 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 135 )

    def testTableNotRenumberedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        renumerator  : TableRenumerator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        repositoryMock.update.return_value = False
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        eventBusMock = Mock()
        renumerator = TableRenumerator(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = renumerator.renumber( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 6 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )