"""
 *
 * Libraries 
 *
"""

import unittest
from src.product.domain import Product
from src.shared.domain  import ProductId
from src.product.domain import ProductName
from src.product.domain import ProductPrice
from src.product.domain import ProductDescription
from src.shared.domain  import RestaurantId
from src.shared.domain  import DomainException

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

    def testValidDataToCreate( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                ProductName( 'Sandwich' ),
                ProductPrice( 3 ),
                ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testInvalidDataToCreate1( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( '' ),
                ProductName( 'Sandwich' ),
                ProductPrice( 3 ),
                ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 109 )
    
    def testInvalidDataToCreate2( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                ProductName( '' ),
                ProductPrice( 3 ),
                ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 124 )
    
    def testInvalidDataToCreate3( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                ProductName( 'Sandwich' ),
                ProductPrice( 0 ),
                ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 126 )
    
    def testInvalidDataToCreate4( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                ProductName( 'Sandwich' ),
                ProductPrice( -5 ),
                ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 126 )
    
    def testInvalidDataToCreate5( self ):
        # Variables
        responseCode : int
        product      : Product
        # Code
        responseCode = 0
        try:
            product = Product.create( 
                ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                ProductName( 'Sandwich' ),
                ProductPrice( 3 ),
                ProductDescription( '' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 125 )
    
    def testProductDeletedSuccess( self ):
        # Variables
        product : Product
        # Code
        product = Product( 
            ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            ProductName( 'Sandwich' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        product.delete()
        self.assertEqual( product.status(), 2 )
    
    def testProductRenamedSuccess( self ):
        # Variables
        product : Product
        # Code
        product = Product( 
            ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            ProductName( 'Hot dog' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        product.rename( ProductName( 'Sandwich' ) )
        self.assertEqual( product.name().value(), 'Sandwich' )
    
    def testProductRevaluedSuccess( self ):
        # Variables
        product : Product
        # Code
        product = Product( 
            ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            ProductName( 'Sandwich' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        product.revalue( ProductPrice( 4 ) )
        self.assertEqual( product.price().value(), 4 )