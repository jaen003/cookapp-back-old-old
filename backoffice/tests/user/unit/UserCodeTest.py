"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain   import UserCode
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
        # Variables
        responseCode : int
        code         : UserCode
        responseCode = 0
        try:
            code = UserCode( '12345' )
            code.match( '12345' )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testInvalidUserCode( self ):
        # Variables
        responseCode : int
        code         : UserCode
        responseCode = 0
        try:
            code = UserCode( '12345' )
            code.match( '12346' )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 148 )

