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

    public class InvalidTableId : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_TABLE_ID = 204;

        /* 
         * 
         * Methods
         *
        */

        public InvalidTableId( string id ) : base( 
            INVALID_TABLE_ID,
            string.Format( "The table id {0} is invalid", id )
        ) {
        }

    }

}