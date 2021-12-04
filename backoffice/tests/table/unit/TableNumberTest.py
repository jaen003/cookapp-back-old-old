"""
 *
 * Libraries 
 *
"""

import unittest
from src.table.domain import TableNumber

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
        number = TableNumber( 33 )
        self.assertTrue( number.isValid() )
    
    def testInvalidTableNumberBecauseItIsLessThanOne( self ):
        number = TableNumber( 0 )
        self.assertFalse( number.isValid() )

    def testInvalidTableNumberBecauseItIsBiggerThanTwoHundredFityFive( self ):
        number = TableNumber( 256 )
        self.assertFalse( number.isValid() )