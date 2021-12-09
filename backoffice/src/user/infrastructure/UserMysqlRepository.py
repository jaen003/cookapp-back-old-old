"""
 *
 * Libraries 
 *
"""

from src.user.domain            import User
from src.shared.domain          import UserEmail
from src.user.domain            import UserName
from src.user.domain            import UserPassword
from src.user.domain            import UserRole
from src.user.domain            import UserRepository
from src.shared.infrastructure  import Database
from src.shared.domain          import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor
from src.user.domain            import UserStatus

"""
 *
 * Classes 
 *
"""

class UserMysqlRepository( UserRepository ):

    """
     *
     * Methods 
     *
    """

    def insert( self, user : User ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO User ( user_email, user_name, user_password, user_role, ' \
                'user_status, rest_id ) VALUES ( %s, %s, %s, %s, %s, %s )'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values = (
                user.email().value(),
                user.name().value(),
                user.password().value(),
                user.role().value(),
                user.status().value(),
                user.restaurantId().value(),
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
                
    def update( self, user : User ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'UPDATE User SET user_name = %s, user_password = %s, user_role = %s, ' \
                'user_status = %s WHERE user_email = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( 
                user.name().value(),
                user.password().value(),
                user.role().value(),
                user.status().value(),
                user.email().value(),
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

    def selectByEmailAndRestaurant( self, email : UserEmail, restaurantId : RestaurantId ) -> User:
        # Variables
        query      : str
        database   : Database
        user       : User
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT user_email, user_name, user_password, user_role, user_status, rest_id ' \
                'FROM User WHERE user_status in ( 1, 3, 4 ) and user_email = %s and rest_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                email.value(),
                restaurantId.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            user = User(
                email        = UserEmail( record[0] ),
                name         = UserName( record[1] ),
                password     = UserPassword( record[2] ),
                role         = UserRole( record[3] ),
                status       = UserStatus( record[4] ),
                restaurantId = RestaurantId( record[5] ),
            )
            return user
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectByEmail( self, email : UserEmail ) -> User:
        # Variables
        query      : str
        database   : Database
        user       : User
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT user_email, user_name, user_password, user_role, user_status, rest_id ' \
                'FROM User WHERE user_status in ( 1, 3, 4 ) and user_email = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                email.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            user = User(
                email        = UserEmail( record[0] ),
                name         = UserName( record[1] ),
                password     = UserPassword( record[2] ),
                role         = UserRole( record[3] ),
                status       = UserStatus( record[4] ),
                restaurantId = RestaurantId( record[5] ),
            )
            return user
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
        users      : list
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT user_email, user_name, user_role, user_status FROM User ' \
                'WHERE user_status in ( 1, 3, 4 ) and rest_id = %s'
        try:
            users      = list()
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( restaurantId.value(), )
            cursor.execute( query, values )
            records  = cursor.fetchall()
            for record in records:
                users.append( {
                    'user_email'  : record[0],
                    'user_name'   : record[1],
                    'user_role'   : record[2],
                    'user_status' : record[3],
                } )
            return users
        except Exception:
            return []
        finally:
            if connection is not None:
                cursor.close()
                connection.close()