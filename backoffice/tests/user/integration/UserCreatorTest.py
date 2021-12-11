"""
 *
 * Libraries 
 *
"""

import unittest
from unittest.mock         import Mock 
from src.user.domain       import User
from src.shared.domain     import UserEmail
from src.user.domain       import UserName
from src.user.domain       import UserPassword
from src.user.domain       import UserRole
from src.shared.domain     import RestaurantId
from src.user.domain       import UserCode
from src.shared.domain     import DomainException
from src.user.application  import UserCreator
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

    __user       : User
    __restaurant : Restaurant

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__user = User( 
            UserEmail( 'harland.sanders@gmail.com' ),
            UserName( 'Harland D. Sanders' ),
            UserPassword( 'IloveKFC' ),
            UserRole( 2 ),
            1,
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            UserCode( '12345' ),
        )
        self.__restaurant = Restaurant(
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            RestaurantName( 'Subway' ),
            1,
        )

    def testAdministratorCreatedSuccessfully( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmail.return_value = None
        volatileRepositoryMock = Mock()
        volatileRepositoryMock.insert.return_value = True
        restaurantRepositoryMock = Mock()
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
            volatileRepository   = volatileRepositoryMock,
        )
        try:
            creator.createAdministrator( 
                email    = UserEmail( 'harland.sanders@gmail.com' ),
                name     = UserName( 'Harland D. Sanders' ),
                password = UserPassword( 'IloveKFC' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testAdministratorNotCreatedBecauseItAlreadyExist( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmail.return_value = self.__user
        restaurantRepositoryMock = Mock()
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createAdministrator( 
                email    = UserEmail( 'harland.sanders@gmail.com' ),
                name     = UserName( 'Harland D. Sanders' ),
                password = UserPassword( 'IloveKFC' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 139 )
    
    def testAdministratorNotCreatedDueToInternalServerError1( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmail.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.insert.return_value = False
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createAdministrator( 
                email    = UserEmail( 'harland.sanders@gmail.com' ),
                name     = UserName( 'Harland D. Sanders' ),
                password = UserPassword( 'IloveKFC' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )
    
    def testAdministratorNotCreatedDueToInternalServerError2( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmail.return_value = None
        repositoryMock.insert.return_value        = False
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.insert.return_value = True
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createAdministrator( 
                email    = UserEmail( 'harland.sanders@gmail.com' ),
                name     = UserName( 'Harland D. Sanders' ),
                password = UserPassword( 'IloveKFC' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )
    
    def testChefCreatedSuccessfully( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createChef( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testChefNotCreatedBecauseItAlreadyExist( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = self.__user
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createChef( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 139 )
    
    def testChefNotCreatedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = None
        repositoryMock.insert.return_value                     = False
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createChef( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )
    
    def testWaiterCreatedSuccessfully( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = None
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createWaiter( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 102 )
    
    def testWaiterNotCreatedBecauseItAlreadyExist( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        responseCode   = 102
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = self.__user
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            creator.createWaiter( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 139 )
    
    def testWaiterNotCreatedDueToInternalServerError( self ):
        # Variables
        responseCode : int
        creator      : UserCreator
        # Code
        repositoryMock = Mock()
        repositoryMock.selectByEmailAndRestaurant.return_value = None
        repositoryMock.insert.return_value                     = False
        restaurantRepositoryMock = Mock()
        restaurantRepositoryMock.selectById.return_value = self.__restaurant
        eventBusMock = Mock()
        creator = UserCreator(
            repository           = repositoryMock,
            restaurantRepository = restaurantRepositoryMock,
            eventBus             = eventBusMock,
        )
        try:
            responseCode = creator.createWaiter( 
                email        = UserEmail( 'harland.sanders@gmail.com' ),
                name         = UserName( 'Harland D. Sanders' ),
                restaurantId = RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 103 )