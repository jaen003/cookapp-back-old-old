"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain   import UserRole
from src.shared.domain import DomainException

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

    def testUserIsAdministrator( self ):
        role = UserRole.administrator()
        self.assertEqual( role.value(), 1 )
    
    def testUserIsChef( self ):
        role = UserRole.chef()
        self.assertEqual( role.value(), 2 )
    
    def testUserIsWaiter( self ):
        role = UserRole.waiter()
        self.assertEqual( role.value(), 3 )

    def testUserCodeValidatedSuccess( self ):
        # Variables
        responseCode : int
        role         : UserRole
        responseCode = 0
        try:
            role = UserRole.waiter()
            role.validate( 2 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )

    def testInvalidUserRole1( self ):
        # Variables
        responseCode : int
        role         : UserRole
        responseCode = 0
        try:
            role = UserRole.waiter()
            role.validate( 1 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 144 )
    
    def testInvalidUserRole2( self ):
        # Variables
        responseCode : int
        role         : UserRole
        responseCode = 0
        try:
            role = UserRole.administrator()
            role.validate( 2 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 144 )
    
    def testInvalidUserRole3( self ):
        # Variables
        responseCode : int
        role         : UserRole
        responseCode = 0
        try:
            role = UserRole.administrator()
            role.validate( 3 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 144 )