"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock     import Mock 
from src.table.domain  import TableNumber
from src.table.domain  import TableFinder
from src.shared.domain import RestaurantId
from src.shared.domain import DomainException
from src.shared.domain import TableId
from src.table.domain  import Table
from src.table.domain  import TableDescription

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
            TableNumber( 50 ),
            TableDescription( 'Nice place' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testTableAlreadyExist( self ):
        # Variables
        finder   : TableFinder
        response : Table
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__table
        finder = TableFinder( repositoryMock )
        response = finder.findByIdAndRestaurant( 
            TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNotNone( response )
    
    def testTableNumberAlreadyExist( self ):
        # Variables
        finder   : TableFinder
        response : Table
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = self.__table
        finder = TableFinder( repositoryMock )
        response = finder.findByNumberAndRestaurant( 
            TableNumber( 13 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNotNone( response )
    
    def testTableNotFound( self ):
        # Variables
        finder   : TableFinder
        response : Table
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        finder = TableFinder( repositoryMock )
        response = finder.findByIdAndRestaurant( 
            TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNone( response )
    
    def testTableNumberNotFound( self ):
        # Variables
        finder   : TableFinder
        response : Table
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        finder = TableFinder( repositoryMock )
        response = finder.findByNumberAndRestaurant( 
            TableNumber( 13 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNone( response )
