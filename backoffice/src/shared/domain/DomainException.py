"""
 *
 * Classes 
 *
"""

class DomainException( Exception ):

    """
     *
     * Parameters 
     *
    """

    __code : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, code : int, message : str ) -> None:
        super().__init__( message )
        self.__code = code

    def code( self ) -> int:
        return self.__code