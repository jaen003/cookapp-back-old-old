"""
 *
 * Libraries 
 *
"""

import unittest
from src.product.domain import ProductPrice

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

    def testValidProductPrice( self ):
        price = ProductPrice( 3300 )
        self.assertTrue( price.isValid() )
    
    def testInvalidProductPrice1( self ):
        price = ProductPrice( 0 )
        self.assertFalse( price.isValid() )

    def testInvalidProductPrice2( self ):
        price = ProductPrice( -1000 )
        self.assertFalse( price.isValid() )