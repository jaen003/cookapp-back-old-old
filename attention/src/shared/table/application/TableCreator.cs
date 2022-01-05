/* 
 * 
 * Libraries
 *
*/

using attention.src.table.domain;
using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.table.application {

    public class TableCreator {

        /* 
         * 
         * Attributes
         *
        */

        private TableRepository _repository;

        /* 
         * 
         * Methods
         *
        */

        public TableCreator( TableRepository repository ) {
            _repository = repository;
        }

        public void create(
            TableId      id,
            TableNumber  number,
            RestaurantId restaurantId
        ) {
            // Variables
            Table table;
            // Code

            table = Table.create( id, number, restaurantId );
            if( !_repository.insert( table ) ) {
                throw new ServerInternalError();
            }
        }

    }

}