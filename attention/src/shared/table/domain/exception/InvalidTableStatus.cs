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

    public class InvalidTableStatus : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_TABLE_STATUS = 206;

        /* 
         * 
         * Methods
         *
        */

        public InvalidTableStatus( int status ) : base( 
            INVALID_TABLE_STATUS,
            string.Format( "The table status {0} is invalid", status )
        ) {
        }

    }

}