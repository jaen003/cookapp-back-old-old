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
from src.product.application import ProductRevalorizer
from src.shared.domain       import EventBus
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
            ProductName( 'Sandwich' ),
            ProductPrice( 3 ),
            ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )

    def testProductRevaluedSuccessfully( self ):
        # Variables
        responseCode : int
        revalorizer  : ProductRevalorizer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__product
        eventBusMock = Mock()
        revalorizer = ProductRevalorizer(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = revalorizer.revalue( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                price        = ProductPrice( 4 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testProductNotRevaluedBecauseItNotFound( self ):
        # Variables
        responseCode : int
        revalorizer  : ProductRevalorizer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        eventBusMock = Mock()
        revalorizer = ProductRevalorizer(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = revalorizer.revalue( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                price        = ProductPrice( 4 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 123 )
    
    def testProductNotRevaluedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        revalorizer  : ProductRevalorizer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__product
        repositoryMock.update.return_value = False
        eventBusMock = Mock()
        revalorizer = ProductRevalorizer(
            repository = repositoryMock,
            eventBus   = eventBusMock,
        )
        try:
            responseCode = revalorizer.revalue( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                price        = ProductPrice( 4 ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )