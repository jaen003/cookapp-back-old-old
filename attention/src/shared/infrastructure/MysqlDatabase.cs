/* 
 * 
 * Libraries
 *
*/

using MySql.Data.MySqlClient;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class MysqlDatabase {

        /* 
         * 
         * Attributes
         *
        */

        private static MysqlDatabase?  _instance = null;
        private        MySqlConnection  _connection;

        /* 
         * 
         * Methods
         *
        */

        private MysqlDatabase() {
            // Variables
            string? user;
            string? password;
            string? host;
            string? port;
            string? database;
            string  mySqlUri;
            // Code
            user     = Environment.GetEnvironmentVariable( "DATABASE_USER" );
            password = Environment.GetEnvironmentVariable( "DATABASE_PASSWORD" );
            port     = Environment.GetEnvironmentVariable( "DATABASE_PORT" );
            host     = Environment.GetEnvironmentVariable( "DATABASE_HOST" );
            database = Environment.GetEnvironmentVariable( "DATABASE_NAME" );
            mySqlUri = string.Format( 
                "username={0};password={1};server={2};port={3};database={4};", 
                user, 
                password, 
                host, 
                port, 
                database 
            );
            _connection = new MySqlConnection( mySqlUri );
        }

        public static MysqlDatabase instance() {
            if( _instance == null ) {
                _instance = new MysqlDatabase();
            }
            return _instance;
        }

        public MySqlConnection connection() {
            return _connection;
        }

    }

}
