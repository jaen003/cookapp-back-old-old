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

    public class TableStatus : IntValueObject {

        /* 
         * 
         * Constants
         *
        */

        private const int ENABLED = 1;
        private const int DELETED = 2;
        private const int BUSY    = 3;

        /* 
         * 
         * Methods
         *
        */

        public TableStatus( int value ) : base( value ) {
            if( !isValid() ) {
                throw new InvalidTableStatus( value );
            }
        }

        public bool isValid() {
            return equals( ENABLED ) || equals( DELETED ) || equals( BUSY );
        }

        public static TableStatus enabled() {
            return new TableStatus( ENABLED );
        }

        public static TableStatus deleted() {
            return new TableStatus( DELETED );
        }

        public static TableStatus busy() {
            return new TableStatus( BUSY );
        }

    }

}