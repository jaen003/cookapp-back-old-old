"""
 *
 * Libraries 
 *
"""

import unittest
from src.user.domain   import User
from src.user.domain   import Chef
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

    def testChefCreatedSuccess( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Chef.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )

    def testChefNotCreatedBecauseTheEmailIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Chef.create( 
                UserEmail( '' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 141 )
    
    def testChefNotCreatedBecauseTheNameIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Chef.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( '' ),
                UserPassword( 'IloveKFC' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 142 )
    
    def testChefNotCreatedBecauseThePasswordIsEmpty( self ):
        # Variables
        responseCode : int
        user         : User
        # Code
        responseCode = 0
        try:
            user = Chef.create( 
                UserEmail( 'harland.sanders@gmail.com' ),
                UserName( 'Harland D. Sanders' ),
                UserPassword( '' ),
                RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            )
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 143 )