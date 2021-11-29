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
     * Parameters 
     *
    """

    __product : Product

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__product = Product( 
            ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            ProductName( 'Sandwich' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testProductCreatedSuccess( self ):
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
    
    def testProductNotCreatedBecauseTheIdIsEmpty( self ):
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
    
    def testProductNotCreatedBecauseTheNameIsEmpty( self ):
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
    
    def testProductNotCreatedBecauseThePriceIsInvalid1( self ):
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
    
    def testProductNotCreatedBecauseThePriceIsInvalid2( self ):
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
    
    def testProductNotCreatedBecauseTheDesciptionIsEmpty( self ):
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
        self.__product.delete()
        self.assertEqual( self.__product.status(), 2 )
    
    def testProductRenamedSuccess( self ):
        self.__product.rename( ProductName( 'Sandwich' ) )
        self.assertEqual( self.__product.name().value(), 'Sandwich' )
    
    def testProductRevaluedSuccess( self ):
        self.__product.revalue( ProductPrice( 4 ) )
        self.assertEqual( self.__product.price().value(), 4 )
    
    def testProductRewritedSuccess( self ):
        self.__product.rewrite( ProductDescription( 'Bread, Tomato, Chicken' ) )
        self.assertEqual( self.__product.description().value(), 'Bread, Tomato, Chicken' )