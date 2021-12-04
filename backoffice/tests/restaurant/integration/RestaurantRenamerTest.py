"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock           import Mock 
from src.restaurant.domain      import Restaurant
from src.shared.domain       import RestaurantId
from src.restaurant.domain      import RestaurantName
from src.shared.domain       import RestaurantId
from src.shared.domain       import DomainException
from src.restaurant.application import RestaurantRenamer

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

    __restaurant : Restaurant

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__restaurant = Restaurant(
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            RestaurantName( 'Subway' ),
            1,
        )

    def testRestaurantRenamedSuccessfully( self ):
        # Variables
        responseCode : int
        renamer      : RestaurantRenamer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByName.return_value = None
        repositoryMock.selectById.return_value   = self.__restaurant
        renamer = RestaurantRenamer(
            repository = repositoryMock,
        )
        try:
            responseCode = renamer.rename( 
                id   = RestaurantId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name = RestaurantName( 'Drive Pizza' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testRestaurantNotRenamedBecauseItAlreadyExists( self ):
        # Variables
        responseCode : int
        renamer      : RestaurantRenamer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByName.return_value = self.__restaurant
        renamer = RestaurantRenamer(
            repository = repositoryMock,
        )
        try:
            responseCode = renamer.rename( 
                id   = RestaurantId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name = RestaurantName( 'Drive Pizza' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 149 )
    
    def testRestaurantNotRenamedBecauseItNotFound( self ):
        # Variables
        responseCode : int
        renamer      : RestaurantRenamer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByName.return_value = None
        repositoryMock.selectById.return_value   = None
        renamer = RestaurantRenamer(
            repository = repositoryMock,
        )
        try:
            responseCode = renamer.rename( 
                id   = RestaurantId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name = RestaurantName( 'Drive Pizza' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 110 )

    def testRestaurantNotRenamedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        renamer      : RestaurantRenamer
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByName.return_value = None
        repositoryMock.update.return_value       = False
        repositoryMock.selectById.return_value   = self.__restaurant
        renamer = RestaurantRenamer(
            repository = repositoryMock,
        )
        try:
            responseCode = renamer.rename( 
                id   = RestaurantId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                name = RestaurantName( 'Drive Pizza' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )