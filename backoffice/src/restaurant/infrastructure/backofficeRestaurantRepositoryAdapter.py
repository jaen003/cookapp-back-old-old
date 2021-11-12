"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain          import Restaurant
from src.restaurant.domain          import RestaurantRepository as Repository
from src.persistence.infrastructure import Database
from src.shared.domain              import RestaurantId
from mysql.connector.connection     import MySQLConnection
from mysql.connector.cursor         import MySQLCursor
from src.restaurant.domain          import RestaurantName

"""
 *
 * Classes 
 *
"""

class RestaurantRepository( Repository ):

    """
     *
     * Methods 
     *
    """

    def insert( self, restaurant : Restaurant ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Restaurant ( rest_id, rest_name, rest_status ) VALUES ( %s, %s, %s )'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values = (
                rest.id().value(),
                rest.name().value(),
                rest.status(),
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

    def selectById( self, id : RestaurantId ) -> Restaurant:
        # Variables
        query      : str
        database   : Database
        restaurant : Restaurant
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT rest_id, rest_name, rest_status FROM Restaurant ' \
                'WHERE rest_status = 1 and rest_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                id.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            restaurant = Restaurant(
                id     = RestaurantId( record[0] ),
                name   = RestaurantName( record[1] ),
                status = record[2],
            )
            return restaurant
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()