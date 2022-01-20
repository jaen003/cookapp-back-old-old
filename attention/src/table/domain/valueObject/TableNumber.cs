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

    public class TableNumber : IntValueObject {

        /* 
         * 
         * Constants
         *
        */

        private const int MINIMUM_ALLOWED_VALUE = 1;
        private const int MAXIMUN_ALLOWED_VALUE = 255;

        /* 
         * 
         * Methods
         *
        */

        public TableNumber( int value ) : base( value ) {
            if( !isValid() ) {
                throw new InvalidTableNumber( value );
            }
        }

        public bool isValid() {
            // Variables
            bool response;
            // Code
            response = isLessThan( MINIMUM_ALLOWED_VALUE ) || 
                isBiggerThan( MAXIMUN_ALLOWED_VALUE );
            return response;
        }

    }

}