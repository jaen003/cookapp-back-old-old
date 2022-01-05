/* 
 * 
 * Libraries
 *
*/

using attention.src.table.domain;
using attention.src.shared.domain;
using attention.src.shared.infrastructure;
using MySql.Data.MySqlClient;

/* 
 * 
 * Classes
 *
*/

namespace attention.src.table.infrastructure {

    public class TableMysqlRepository : TableRepository {

        /* 
         * 
         * Methods
         *
        */

        public TableMysqlRepository() {
        }

        public bool insert( Table table ) {
            // Variables
            MysqlDatabase   database;
            MySqlConnection connection;
            MySqlCommand    command;
            string          query;
            // Code
            query = "INSERT INTO Dining_Table ( tab_id, tab_number, tab_status, " +
                    "rest_id ) VALUES ( @id, @number, @status, @restaurantId )";
            try {
                database   = MysqlDatabase.instance();
                connection = database.connection();
                connection.Open();                
                command = connection.CreateCommand();
                command.CommandText = query;
                command.Parameters.AddWithValue( "@id", table.id().value() );
                command.Parameters.AddWithValue( "@number", table.number().value() );
                command.Parameters.AddWithValue( "@status", table.status().value() );
                command.Parameters.AddWithValue( "@restaurantId", table.restaurantId().value() );
                command.ExecuteNonQuery();
                connection.Close();
                return true;
            } catch( MySqlException ) {
                return false;
            }
        }
        public bool update( Table table ) {
            // Variables
            MysqlDatabase   database;
            MySqlConnection connection;
            MySqlCommand    command;
            string          query;
            // Code
            query = "UPDATE Dining_Table SET tab_status = @status WHERE tab_id = @id";
            try {
                database   = MysqlDatabase.instance();
                connection = database.connection();
                connection.Open();                
                command = connection.CreateCommand();
                command.CommandText = query;
                command.Parameters.AddWithValue( "@status", table.status().value() );
                command.Parameters.AddWithValue( "@id", table.id().value() );
                command.ExecuteNonQuery();
                connection.Close();
                return true;
            } catch( MySqlException ) {
                return false;
            }
        }
        public Table? select( Specifications specifications ) {
            // Variables
            MysqlDatabase   database;
            MySqlConnection connection;
            MySqlCommand    command;
            string          query;
            MySqlDataReader reader;
            Table           table;
            // Code
            query = "SELECT * Dining_Table WHERE " + specifications.serialize();
            try {
                database   = MysqlDatabase.instance();
                connection = database.connection();
                connection.Open();                
                command = connection.CreateCommand();
                command.CommandText = query;
                reader = command.ExecuteReader();
                table  = new Table( 
                    new TableId( reader["tab_id"].ToString() ?? "" ),
                    new TableNumber( Int32.Parse( reader["tab_number"].ToString() ?? "" ) ),
                    new TableStatus( Int32.Parse( reader["tab_status"].ToString() ?? "" ) ),
                    new RestaurantId( reader["rest_id"].ToString() ?? "" )
                );
                connection.Close();
                return table;
            } catch( MySqlException ) {
                return null;
            }
        }

    }

}