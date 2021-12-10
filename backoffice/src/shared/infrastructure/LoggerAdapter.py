"""
 *
 * Libraries 
 *
"""

import logging
from src.shared.domain import Logger

"""
 *
 * Classes
 *
"""

class LoggerAdapter( Logger ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        logging.basicConfig(
            filename = "backoffice.log",
            filemode = 'w',
            level    = logging.DEBUG,
        )
    
    def info( self, message : str ) -> None:
        logging.info( message )
    
    def fatal( self, message : str ) -> None:
        logging.critical( message )

    def warning( self, message : str ) -> None:
        logging.warning( message )