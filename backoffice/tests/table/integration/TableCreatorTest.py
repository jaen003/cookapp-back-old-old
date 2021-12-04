"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock         import Mock 
from src.table.domain      import Table
from src.shared.domain     import TableId
from src.table.domain      import TableNumber
from src.table.domain      import TableDescription
from src.shared.domain     import RestaurantId
from src.shared.domain     import DomainException
from src.table.application import TableCreator
from src.restaurant.domain import Restaurant
from src.restaurant.domain import RestaurantName

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

    __table      : Table
    __restaurant : Restaurant

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__table = Table( 
            TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
            TableNumber( 17 ),
            TableDescription( 'Nice place' ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
        )
        self.__restaurant = Restaurant(
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            RestaurantName( 'Subway' ),
            1,
        )

    def testTableCreatedSuccessfully( self ):
        # Variables
        responseCode : int
        creator      : TableCreator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = TableCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            responseCode = creator.create( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 17 ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testTableNotCreatedBecauseItAlreadyExist( self ):
        # Variables
        responseCode : int
        creator      : TableCreator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = self.__table
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = TableCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            responseCode = creator.create( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 17 ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 137 )
    
    def testTableNotCreatedBecauseTheRestaurantWasNotFound( self ):
        # Variables
        responseCode : int
        creator      : TableCreator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = None
        eventBusMock = Mock()
        creator = TableCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            responseCode = creator.create( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 17 ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 110 )
    
    def testTableNotCreatedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        creator      : TableCreator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByNumberAndRestaurant.return_value = None
        repositoryMock.insert.return_value = False
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = TableCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            responseCode = creator.create( 
                id           = TableId( 'f727c0e0-31fc-11ec-8ce7-f91f9c1d88b1' ),
                number       = TableNumber( 17 ),
                description  = TableDescription( 'Nice place' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )