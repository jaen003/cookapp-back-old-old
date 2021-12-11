"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock      import Mock 
from src.product.domain import ProductPrice
from src.product.domain import ProductFinder
from src.shared.domain  import RestaurantId
from src.shared.domain  import DomainException
from src.shared.domain  import ProductId
from src.product.domain import ProductName
from src.product.domain import Product
from src.product.domain import ProductDescription

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

    def testProductAlreadyExist( self ):
        # Variables
        finder   : ProductFinder
        response : Product
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = self.__product
        finder   = ProductFinder( repositoryMock )
        response = finder.findByIdAndRestaurant( 
            ProductId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNotNone( response )
    
    def testProductNameAlreadyExist( self ):
        # Variables
        finder   : ProductFinder
        response : Product
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = self.__product
        finder = ProductFinder( repositoryMock )
        response = finder.findByNameAndRestaurant( 
            ProductName( 'Sandwich' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNotNone( response )
    
    def testProductNotFound( self ):
        # Variables
        finder   : ProductFinder
        response : Product
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByIdAndRestaurant.return_value = None
        finder = ProductFinder( repositoryMock )
        response = finder.findByIdAndRestaurant(
            ProductName( 'Sandwich' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNone( response )
    
    def testProductNameNotFound( self ):
        # Variables
        finder   : ProductFinder
        response : Product
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNameAndRestaurant.return_value = None
        finder = ProductFinder( repositoryMock )
        response = finder.findByNameAndRestaurant(
            ProductName( 'Sandwich' ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.assertIsNone( response )
