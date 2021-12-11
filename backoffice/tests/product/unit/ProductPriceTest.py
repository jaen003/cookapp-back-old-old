"""
 *
 * Libraries 
 *
"""

import unittest
from src.product.domain import ProductPrice
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

    def testValidProductPrice( self ):
        # Variables
        responseCode : int
        price        : ProductPrice
        responseCode = 0
        try:
            price = ProductPrice( 3300 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
        self.assertTrue( price.isValid() )
    
    def testInvalidProductPrice1( self ):
        # Variables
        responseCode : int
        price        : ProductPrice
        responseCode = 0
        try:
            price = ProductPrice( 0 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 126 )

    def testInvalidProductPrice2( self ):
        # Variables
        responseCode : int
        price        : ProductPrice
        responseCode = 0
        try:
            price = ProductPrice( -1000 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 126 )