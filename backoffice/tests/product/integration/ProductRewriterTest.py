"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock           import Mock 
from src.product.domain      import Product
from src.shared.domain       import ProductId
from src.product.domain      import ProductName
from src.product.domain      import ProductDescription
from src.shared.domain       import RestaurantId
from src.shared.domain       import DomainException
from src.product.application import ProductRewriter
from src.product.domain      import ProductPrice

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
            ProductName( 'Hot dog' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testProductRewritedSuccessfully( self ):
        # Variables
        responseCode : int
        rewriter     : ProductRewriter
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__product
        eventBusMock = Mock()
        rewriter = ProductRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            rewriter.rewrite( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testProductNotRewritedBecauseItNotFound( self ):
       # Variables
        responseCode : int
        rewriter     : ProductRewriter
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        eventBusMock = Mock()
        rewriter = ProductRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            rewriter.rewrite( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 123 )

    def testProductNotRewritedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        rewriter     : ProductRewriter
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__product
        repositoryMock.update.return_value = False
        eventBusMock = Mock()
        rewriter = ProductRewriter(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            rewriter.rewrite( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )