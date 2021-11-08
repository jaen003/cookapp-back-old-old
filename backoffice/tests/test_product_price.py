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

    def test_valid_price( self ):
        price = ProductPrice( 3300 )
        self.assertTrue( price.isValid() )
    
    def test_invalid_price_1( self ):
        price = ProductPrice( 0 )
        self.assertFalse( price.isValid() )

    def test_invalid_price_2( self ):
        price = ProductPrice( -1000 )
        self.assertFalse( price.isValid() )