"""
 *
 * Libraries 
 *
"""

from src.product.domain         import Product
from src.product.domain         import ProductName
from src.product.domain         import ProductRepository as Repository
from src.shared.infrastructure  import Database
from src.shared.domain          import ProductId
from src.shared.domain          import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor
from src.product.domain         import ProductPrice
from src.product.domain         import ProductDescription
from src.product.domain         import ProductStatus

"""
 *
 * Classes 
 *
"""

class ProductRepository( Repository ):

    """
     *
     * Methods 
     *
    """

    def insert( self, product : Product ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Product ( prod_id, prod_name, prod_price, ' \
                'prod_description, prod_status, rest_id ) ' \
                'VALUES ( %s, %s, %s, %s, %s, %s )'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values = (
                product.id().value(),
                product.name().value(),
                product.price().value(),
                product.description().value(),
                product.status().value(),
                product.restaurantId().value(),
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
                
    def update( self, product : Product ) -> bool:
        # Variables
        query      : str
        database   : Database
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'UPDATE Product SET prod_name = %s, prod_price = %s, ' \
                'prod_status = %s, prod_description = %s WHERE prod_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( 
                product.name().value(),
                product.price().value(),
                product.status().value(),
                product.description().value(),
                product.id().value(),
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

    def selectByIdAndRestaurant( self, id : ProductId, restaurantId : RestaurantId ) -> Product:
        # Variables
        query      : str
        database   : Database
        product    : Product
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, prod_status, rest_id ' \
                'FROM Product WHERE prod_status = 1 and prod_id = %s and rest_id = %s'
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
            product = Product(
                id           = ProductId( record[0] ),
                name         = ProductName( record[1] ),
                price        = ProductPrice( record[2] ),
                description  = ProductDescription( record[3] ),
                status       = ProductStatus( record[4] ),
                restaurantId = RestaurantId( record[5] ),
            )
            return product
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> Product:
        # Variables
        query      : str
        database   : Database
        product    : Product
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, prod_status, rest_id ' \
                'FROM Product WHERE prod_status = 1 and prod_name = %s and rest_id = %s'
        try:
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = (
                name.value(),
                restaurantId.value(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            if record is None:
                return None
            product = Product(
                id           = ProductId( record[0] ),
                name         = ProductName( record[1] ),
                price        = ProductPrice( record[2] ),
                description  = ProductDescription( record[3] ),
                status       = ProductStatus( record[4] ),
                restaurantId = RestaurantId( record[5] ),
            )
            return product
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectAllByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> list:
        # Variables
        query      : str
        database   : Database
        products   : list
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, rest_id ' \
                'FROM Product WHERE prod_status = 1 and prod_name ' \
                'LIKE "%{}%" and rest_id = %s'.format( name.value() )
        try:
            products   = list()
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( restaurantId.value(), )
            cursor.execute( query, values )
            records = cursor.fetchall()
            for record in records:
                products.append( {
                    'prod_id'          : record[0],
                    'prod_name'        : record[1],
                    'prod_price'       : record[2],
                    'prod_description' : record[3],
                    'rest_id'          : record[4],
                } )
            return products
        except Exception:
            return []
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def selectAllByRestaurant( self, restaurantId : RestaurantId ) -> list:
        # Variables
        query      : str
        database   : Database
        products   : list
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, rest_id ' \
                'FROM Product WHERE prod_status = 1 and rest_id = %s'
        try:
            products   = list()
            database   = Database()
            connection = database.connect()
            cursor     = connection.cursor()
            values     = ( restaurantId.value(), )
            cursor.execute( query, values )
            records = cursor.fetchall()
            for record in records:
                products.append( {
                    'prod_id'          : record[0],
                    'prod_name'        : record[1],
                    'prod_price'       : record[2],
                    'prod_description' : record[3],
                    'rest_id'          : record[4],
                } )
            return products
        except Exception:
            return []
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
                