/* 
 * 
 * Libraries 
 *
*/

using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.table.domain {

    public class Table {

        /* 
         * 
         * Methods
         *
        */

        private TableId      _id;
        private TableNumber  _number;
        private TableStatus  _status;
        private RestaurantId _restaurantId;

        /* 
         * 
         * Methods
         *
        */

        public Table(
            TableId      id,
            TableNumber  number,
            TableStatus  status,
            RestaurantId restaurantId
        ) {
            _id           = id;
            _number       = number;
            _status       = status;
            _restaurantId = restaurantId;
        }

        public TableId id() {
            return _id;
        }

        public TableNumber number() {
            return _number;
        }

        public TableStatus status() {
            return _status;
        }

        public RestaurantId restaurantId() {
            return _restaurantId;
        }

        public static Table create(
            TableId      id,
            TableNumber  number,
            RestaurantId restaurantId
        ) {
            // Variables
            Table table;
            // Code
            table = new Table( id, number, TableStatus.enabled(), restaurantId );
            return table;
        }

    }

}