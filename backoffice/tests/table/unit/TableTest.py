"""
 *
 * Libraries 
 *
"""

import unittest
from src.table.domain  import Table
from src.shared.domain import TableId
from src.table.domain  import TableNumber
from src.table.domain  import TableDescription
from src.shared.domain import RestaurantId
from src.shared.domain import DomainException

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
            TableNumber( 3 ),
            TableDescription( 'Nice place' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testTableCreatedSuccess( self ):
        # Variables
        responseCode : int
        table        : Table
        # Code
        responseCode = 0
        try:
            table = Table.create( 
                TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                TableNumber( 3 ),
                TableDescription( 'Nice place' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )

    def testTableNotCreatedBecauseTheIdIsEmpty( self ):
        # Variables
        responseCode : int
        table        : Table
        # Code
        responseCode = 0
        try:
            table = Table.create( 
                TableId( '' ),
                TableNumber( 5 ),
                TableDescription( 'Nice place' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 138 )
    
    def testTableNotCreatedBecauseTheNumberIsInvalid( self ):
        # Variables
        responseCode : int
        table        : Table
        # Code
        responseCode = 0
        try:
            table = Table.create( 
                TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                TableNumber( 0 ),
                TableDescription( 'Nice place' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 133 )
    
    def testTableNotCreatedBecauseTheNumberIsInvalid2( self ):
        # Variables
        responseCode : int
        table        : Table
        # Code
        responseCode = 0
        try:
            table = Table.create( 
                TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                TableNumber( 256 ),
                TableDescription( 'Nice place' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 133 )
    
    def testTableDeletedSuccess( self ):
        self.__table.delete()
        self.assertEqual( self.__table.status().value(), 2 )
    
    def testTableRenumberedSuccess( self ):
        self.__table.renumber( TableNumber( 4 ) )
        self.assertEqual( self.__table.number().value(), 4 )
    
    def testTableRewritedSuccess( self ):
        self.__table.rewrite( TableDescription( 'Very very well' ) )
        self.assertEqual( self.__table.description().value(), 'Very very well' )