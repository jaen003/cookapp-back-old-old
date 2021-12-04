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

    __message : str
    __code    : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, code : int, message : str ) -> None:
        self.__code = code
        self.__message = message
    
    def message( self ) -> str:
        return self.__message

    def code( self ) -> int:
        return self.__code