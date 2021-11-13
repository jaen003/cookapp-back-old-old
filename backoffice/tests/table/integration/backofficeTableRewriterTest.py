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
from src.table.application import TableRewriter

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

    def testTableRewritedSuccessfully( self ):
        # Variables
        responseCode : int
        rewriter     : TableRewriter
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        eventBusMock = Mock()
        rewriter = TableRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = rewriter.rewrite( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testTableNotRewritedBecauseItNotFound( self ):
       # Variables
        responseCode : int
        rewriter     : TableRewriter
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        eventBusMock = Mock()
        rewriter = TableRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = rewriter.rewrite( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 135 )

    def testTableNotRewritedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        rewriter     : TableRewriter
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        repositoryMock.update.return_value = False
        eventBusMock = Mock()
        rewriter = TableRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = rewriter.rewrite( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )