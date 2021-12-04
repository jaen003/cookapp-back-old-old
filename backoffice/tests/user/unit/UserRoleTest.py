"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain import UserRole

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
        role = UserRole.waiter()
        self.assertTrue( role.validate( 2 ) )

    def testInvalidUserRole( self ):
        role = UserRole.waiter()
        self.assertFalse( role.validate( 1 ) )
    
    def testInvalidUserRole1( self ):
        role = UserRole.administrator()
        self.assertFalse( role.validate( 2 ) )
    
    def testInvalidUserRole3( self ):
        role = UserRole.administrator()
        self.assertFalse( role.validate( 3 ) )