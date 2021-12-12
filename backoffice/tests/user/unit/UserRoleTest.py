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
    
    def testUserRoleIsValid1( self ):
        # Variables
        responseCode : int
        role         : UserRole
        # Code
        responseCode = 0
        try:
            role = UserRole( 1 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testUserRoleIsValid2( self ):
        # Variables
        responseCode : int
        role         : UserRole
        # Code
        responseCode = 0
        try:
            role = UserRole( 2 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testUserRoleIsValid3( self ):
        # Variables
        responseCode : int
        role         : UserRole
        # Code
        responseCode = 0
        try:
            role = UserRole( 3 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testInvalidUserRole( self ):
        # Variables
        responseCode : int
        role         : UserRole
        # Code
        responseCode = 0
        try:
            role = UserRole( 4 )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 144 )