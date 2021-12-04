"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain   import User
from src.user.domain   import Waiter
from src.shared.domain import UserEmail
from src.user.domain   import UserName
from src.user.domain   import UserPassword
from src.shared.domain import RestaurantId
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

    def testWaiterCreatedSuccess( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Waiter.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )

    def testWaiterNotCreatedBecauseTheEmailIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Waiter.create( 
                UserEmail( '' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 141 )
    
    def testWaiterNotCreatedBecauseTheNameIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Waiter.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( '' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 142 )
    
    def testWaiterNotCreatedBecauseThePasswordIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Waiter.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( '' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 143 )