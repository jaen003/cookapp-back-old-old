"""
 *
 * Libraries 
 *
"""

import unittest
from src.restaurant.domain import Restaurant
from src.shared.domain     import RestaurantId
from src.restaurant.domain import RestaurantName
from src.shared.domain     import RestaurantId
from src.shared.domain     import DomainException

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

    __restaurant : Restaurant

    """
     *
     * Methods 
     *
    """

    def setUp( self ):
        self.__restaurant = Restaurant(
            RestaurantId( '43fd2ede-699d-4602-b6e3-3987923a28e4' ),
            RestaurantName( 'Subway' ),
            1,
        )

    def testRestaurantCreatedSuccess( self ):
        # Variables
        responseCode : int
        restaurant   : Restaurant
        # Code
        responseCode = 0
        try:
            restaurant = Restaurant.create()
        except DomainException as exc:
            responseCode = exc.code()
        self.assertEqual( responseCode, 0 )
    
    def testRestaurantRenamedSuccess( self ):
        self.__restaurant.rename( RestaurantName( 'Drive pizza' ) )
        self.assertEqual( self.__restaurant.name().value(), 'Drive pizza' )