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

    public class TableId : UuidValueObject {

        /* 
         * 
         * Methods
         *
        */

        public TableId( string value ) : base( value ) {
            if( isEmpty() ) {
                throw new InvalidTableId( value );
            }
        }

    }

}