"""
 *
 * Libraries 
 *
"""

from src.shared.domain import IntValueObject

"""
 *
 * Classes 
 *
"""

class UserRole( IntValueObject ):

    """
     *
     * Consts 
     *
    """

    __ADMINISTRATOR = 1
    __CHEF          = 2
    __WAITER        = 3


    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )

    @classmethod
    def administrator( cls ): # -> UserRole
        self = cls( cls.__ADMINISTRATOR )
        return self
    
    @classmethod
    def chef( cls ): # -> UserRole
        self = cls( cls.__CHEF )
        return self
    
    @classmethod
    def waiter( cls ): # -> UserRole
        self = cls( cls.__WAITER )
        return self
