"""
 *
 * Libraries 
 *
"""

import os
from mysql.connector.pooling    import MySQLConnectionPool
from mysql.connector.connection import MySQLConnection
from .LoggerAdapter             import LoggerAdapter
from src.shared.domain          import Logger

"""
 *
 * Classes 
 *
"""

class Singleton( type ):

    """
     *
     * Parameters 
     *
    """

    __instances = {}

    """
     *
     * Methods 
     *
    """

    def __call__( cls, *args, **kwargs ):
        if cls not in cls.__instances:
            instance = super().__call__( *args, **kwargs )
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class Database( metaclass = Singleton ):

    """
     *
     * Parameters 
     *
    """

    __connectionPool : MySQLConnectionPool

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        # Variables
        password : str
        user     : str
        host     : str
        database : str
        port     : str
        logger   : Logger
        # Code
        password = os.getenv( 'DATABASE_PASSWORD' )
        user     = os.getenv( 'DATABASE_USER' )
        database = os.getenv( 'DATABASE_NAME' )
        host     = os.getenv( 'DATABASE_HOST' )
        port     = os.getenv( 'DATABASE_PORT' )
        try:
            self.__connectionPool = MySQLConnectionPool(
                pool_name          = 'DatabasePool',
                pool_size          = 10,
                pool_reset_session = True,
                host               = host,
                user               = user,
                password           = password,
                database           = database,
                port               = port,
            )
        except Exception:
            logger = LoggerAdapter()
            logger.fatal( 'Failed to connect to database!' )

    def connect( self ):
        # Variables
        connection : MySQLConnection
        logger     : Logger
        # Code
        try:
            connection = self.__connectionPool.get_connection()
            return connection
        except Exception:
            logger = LoggerAdapter()
            logger.fatal( 'Failed getting connection; pool exhausted' )
            return None
