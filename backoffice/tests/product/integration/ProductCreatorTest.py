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
from src.product.domain      import ProductPrice
from src.product.domain      import ProductDescription
from src.shared.domain       import RestaurantId
from src.shared.domain       import DomainException
from src.product.application import ProductCreator
from src.restaurant.domain   import Restaurant
from src.restaurant.domain   import RestaurantName

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

    __product    : Product
    __restaurant : Restaurant

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
        self.__restaurant = Restaurant(
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            RestaurantName( 'Subway' ),
            1,
        )

    def testProductCreatedSuccessfully( self ):
        # Variables
        responseCode : int
        creator      : ProductCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = ProductCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.create( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name         = ProductName( 'Sandwich' ),
                price        = ProductPrice( 3 ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testProductNotCreatedBecauseItAlreadyExist( self ):
        # Variables
        responseCode : int
        creator      : ProductCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = self.__product
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = ProductCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.create( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name         = ProductName( 'Sandwich' ),
                price        = ProductPrice( 3 ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 162 )
    
    def testProductNotCreatedBecauseTheRestaurantWasNotFound( self ):
        # Variables
        responseCode : int
        creator      : ProductCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = None
        eventBusMock = Mock()
        creator = ProductCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.create( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name         = ProductName( 'Sandwich' ),
                price        = ProductPrice( 3 ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 110 )
    
    def testProductNotCreatedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        creator      : ProductCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = None
        repositoryMock.insert.return_value = False
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = ProductCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.create( 
                id           = ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name         = ProductName( 'Sandwich' ),
                price        = ProductPrice( 3 ),
                description  = ProductDescription( 'Bread, Onion, Tomato, Chicken' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )