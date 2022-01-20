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

    public class InvalidTableNumber : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_TABLE_NUMBER = 205;

        /* 
         * 
         * Methods
         *
        */

        public InvalidTableNumber( int number ) : base( 
            INVALID_TABLE_NUMBER,
            string.Format( "The table number {0} is invalid", number )
        ) {
        }

    }

}