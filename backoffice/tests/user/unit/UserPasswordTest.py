"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain import UserPassword

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

    def testUserWeakPassword( self ):
        password = UserPassword.weak()
        self.assertEqual( len( password.value() ), 8 )
    
    def testUserPasswordIsValid( self ):
        # Variables
        isValid       : bool
        allowedValues : str
        password      : UserPassword
        # Code
        allowedValues = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-&+'
        isValid       = True
        password      = UserPassword.weak()
        for c in password.value():
            if c not in allowedValues:
                isValid = False
                break
        self.assertTrue( isValid )

