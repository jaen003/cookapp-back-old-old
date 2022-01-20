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

    public class TableAlreadyCreated : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int TABLE_ALREADY_CREATED = 207;

        /* 
         * 
         * Methods
         *
        */

        public TableAlreadyCreated( TableId id ) : base( 
            TABLE_ALREADY_CREATED,
            string.Format( "The table {0} has already been created", id.value() )
        ) {
        }

    }

}