"""
 *
 * Libraries 
 *
"""

from src.shared.domain         import StringValueObject
from random                    import choice
from time                      import mktime
from datetime                  import datetime
from datetime                  import timedelta
from .InvalidUserCodeException import InvalidUserCodeException

"""
 *
 * Classes 
 *
"""

class UserCode( StringValueObject ):

    """
     *
     * Consts 
     *
    """

    __ALLOWED_VALUES  = '0123456789'
    __SHORT_SIZE      = 5
    __EXPIRATION_TIME = 5 # 5 minutes

    """
     *
     * Parameters 
     *
    """

    __expiresAt : int

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if not self.isValid():
            raise InvalidUserCodeException( value )
        dateNow          = datetime.now()
        finalDate        = dateNow + timedelta( minutes = self.__EXPIRATION_TIME )
        self.__expiresAt = int( mktime( finalDate.timetuple() ) )
    
    @classmethod
    def short( cls ): # -> StringValueObject
        # Variables
        code : str
        # Code
        code = ''
        code = code.join( [ choice( cls.__ALLOWED_VALUES ) for i in range( cls.__SHORT_SIZE ) ] )
        self = cls( code )
        return self
    
    def match( self, code : str ) -> None:
        # Variables
        isMatch : bool
        # Code
        isMatch = False
        dateNow = int( mktime( datetime.now().timetuple() ) )
        if dateNow < self.__expiresAt:
            if self.equals( code ):
                isMatch = True
        if not isMatch:
            raise InvalidUserCodeException( code )
    
    def isValid( self ):
        if self.isLongerThan( self.__SHORT_SIZE - 1 ):
            return True
        return False