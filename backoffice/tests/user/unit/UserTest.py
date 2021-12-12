"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain   import User
from src.shared.domain import UserEmail
from src.user.domain   import UserName
from src.user.domain   import UserPassword
from src.user.domain   import UserRole
from src.shared.domain import RestaurantId
from src.user.domain   import UserCode
from src.shared.domain import DomainException
from src.user.domain   import UserStatus

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

    __user : User

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
    
    def testUserDeletedSuccess( self ):
        self.__user.delete()
        self.assertEqual( self.__user.status().value(), 2 )
    
    def testUserRenameSuccess( self ):
        self.__user.rename( UserName( 'Harland D.' ) )
        self.assertEqual( self.__user.name().value(), 'Harland D.' )
    
    def testUserInsuredSuccess( self ):
        self.__user.insure( UserPassword( 'Password' ) )
        self.assertEqual( self.__user.password().value(), 'Password' )
    
    def testUserRelocatedSuccess1( self ):
        # Variables
        responseCode : int
        # Code
        responseCode = 0
        try:
            self.__user.relocateAsWaiter()
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
        self.assertEqual( self.__user.role().value(), 3 )
    
    def testUserRelocatedSuccess2( self ):
        # Variables
        responseCode : int
        # Code
        responseCode = 0
        try:
            self.__user.relocateAsChef()
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
        self.assertEqual( self.__user.role().value(), 2 )
    
    def testUserNotRelocated1( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        user = User( 
            UserEmail( 'harland.sanders@gmail.com' ),
            UserName( 'Harland D. Sanders' ),
            UserPassword( 'IloveKFC' ),
            UserRole( 1 ),
            UserStatus( 3 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            UserCode( '12345' ),
        )
        try:
            user.relocateAsChef()
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 164 )
    
    def testUserNotRelocated2( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        user = User( 
            UserEmail( 'harland.sanders@gmail.com' ),
            UserName( 'Harland D. Sanders' ),
            UserPassword( 'IloveKFC' ),
            UserRole( 1 ),
            UserStatus( 3 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            UserCode( '12345' ),
        )
        try:
            user.relocateAsWaiter()
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 164 )
    
    def testUserIsEnabled( self ):
        # Variables
        user : User
        # Code
        user = User( 
            UserEmail( 'harland.sanders@gmail.com' ),
            UserName( 'Harland D. Sanders' ),
            UserPassword( 'IloveKFC' ),
            UserRole( 1 ),
            UserStatus( 3 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            UserCode( '12345' ),
        )
        self.assertTrue( user.status().isDisabled() )
    
    def testUserIsBlocked( self ):
        # Variables
        user : User
        # Code
        user = User( 
            UserEmail( 'harland.sanders@gmail.com' ),
            UserName( 'Harland D. Sanders' ),
            UserPassword( 'IloveKFC' ),
            UserRole( 1 ),
            UserStatus( 4 ),
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            UserCode( '12345' ),
        )
        self.assertTrue( user.status().isBlocked() )
    
    def testUserCodeValidatedSuccess( self ):
        # Variables
        responseCode : int
        # Code
        responseCode = 0
        try:
            self.__user.validate( UserCode( '12345' ) )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testUserCodeRenovatedSuccess( self ):
        self.__user.renovateCode( UserCode( '45321' ) )
        self.assertEqual( self.__user.code().value(), '45321' )