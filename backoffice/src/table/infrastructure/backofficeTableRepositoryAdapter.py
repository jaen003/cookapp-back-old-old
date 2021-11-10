"""
 *
 * Libraries 
 *
"""

from src.table.domain               import Table
from src.table.domain               import TableNumber
from src.table.domain               import TableDescription
from src.table.domain               import TableRepository as Repository
from src.persistence.infrastructure import Database
from src.shared.domain              import TableId
from src.shared.domain              import RestaurantId
from mysql.connector.connection     import MySQLConnection
from mysql.connector.cursor         import MySQLCursor

"""
 *
 * Classes 
 *
"""

class TableRepository( Repository ):

    """
     *
     * Methods 
     *
    """

    def insert( self, table : Table ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Dining_Table ( tab_id, tab_number, tab_description, ' \
                'tab_status, rest_id ) VALUES ( %s, %s, %s, %s, %s )'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values = (
                table.id().value(),
                table.number().value(),
                table.description().value(),
                table.status(),
                table.restaurantId().value(),
            )
            cursor.execute( query, values )
            connection.commit()
            return True
        except Exception:
            return False
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
                
    def update( self, table : Table ) -> bool:
        # Variables
        query        : str
        database     : Database
        values       : tuple
        connection   : MySQLConnection
        cursor       : MySQLCursor
        # Code
        query = 'UPDATE Dining_Table SET tab_number = %s, tab_description = %s, ' \
                'tab_status = %s WHERE tab_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( 
                table.number().value(),
                table.description().value(),
                table.status(),
                table.id().value(),
            )
            cursor.execute( query, values )
            connection.commit()
            return True
        except Exception:
            return False
        finally:
            if connection is not None:
                cursor.close()
                connection.close()

    def selectByIdAndRestaurant( self, id : TableId, restaurantId : RestaurantId ) -> Table:
        # Variables
        query      : str
        database   : Database
        table      : Table
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT tab_id, tab_number, tab_description, tab_status, rest_id ' \
                'FROM Dining_Table WHERE tab_status = 1 and tab_id = %s and rest_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                id.value(),
                restaurantId.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            table = Table(
                id           = TableId( record[0] ),
                number       = TableNumber( record[1] ),
                description  = TableDescription( record[2] ),
                status       = record[3],
                restaurantId = RestaurantId( record[4] ),
            )
            return table
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectByNumberAndRestaurant( self, number : TableNumber, restaurantId : RestaurantId ) -> Table:
        # Variables
        query      : str
        database   : Database
        table      : Table
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT tab_id, tab_number, tab_description, tab_status, rest_id ' \
                'FROM Dining_Table WHERE tab_status = 1 and tab_number = %s and rest_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                number.value(),
                restaurantId.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            table = Table(
                id           = TableId( record[0] ),
                number       = TableNumber( record[1] ),
                description  = TableDescription( record[2] ),
                status       = record[3],
                restaurantId = RestaurantId( record[4] ),
            )
            return table
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectAllByRestaurant( self, restaurantId : RestaurantId ) -> list:
        # Variables
        query      : str
        database   : Database
        tables     : list
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT tab_id, tab_number, tab_description FROM Dining_Table ' \
                'WHERE tab_status = 1 and rest_id = %s'
        try:
            tables     = list()
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( restaurantId.value(), )
            cursor.execute( query, values )
            records  = cursor.fetchall()
            for record in records:
                tables.append( {
                    'tab_id'          : record[0],
                    'tab_number'      : record[1],
                    'tab_description' : record[2],
                } )
            return tables
        except Exception as exc:
            return []
        finally:
            if connection is not None:
                cursor.close()
                connection.close()              
                