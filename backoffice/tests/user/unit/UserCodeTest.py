"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain import UserCode

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

    def testUserShortCode( self ):
        code = UserCode.short()
        self.assertEqual( len( code.value() ), 5 )
    
    def testUserCodeIsValid( self ):
        # Variables
        isValid       : bool
        allowedValues : str
        code          : UserCode
        # Code
        allowedValues = '0123456789'
        isValid       = True
        code          = UserCode.short()
        for c in code.value():
            if c not in allowedValues:
                isValid = False
                break
        self.assertTrue( isValid )
    
    def testUserCodeValidatedSuccess( self ):
        code = UserCode( '12345' )
        self.assertTrue( code.validate( '12345' ) )
    
    def testInvalidUserCode( self ):
        code = UserCode( '12345' )
        self.assertFalse( code.validate( '12346' ) )

