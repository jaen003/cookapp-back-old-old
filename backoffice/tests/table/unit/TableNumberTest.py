"""
 *
 * Libraries 
 *
"""

import unittest
from src.table.domain  import TableNumber
from src.shared.domain import DomainException

"""
 *
 * Classes 
 *
"""

class TestSuite( unittest.TestCase ):

    """
     *
     * Methods 
     *
    """

    def testValidTableNumber( self ):
        # Variables
        responseCode : int
        number       : TableNumber
        # Code
        responseCode = 0
        try:
            number = TableNumber( 33 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
        self.assertTrue( number.isValid() )
    
    def testInvalidTableNumberBecauseItIsLessThanOne( self ):
        # Variables
        responseCode : int
        number       : TableNumber
        # Code
        responseCode = 0
        try:
            number = TableNumber( 0 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 133 )

    def testInvalidTableNumberBecauseItIsBiggerThanTwoHundredFityFive( self ):
        # Variables
        responseCode : int
        # Code
        responseCode = 0
        try:
            number = TableNumber( 256 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 133 )