/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class RestaurantId : UuidValueObject {

        /* 
         * 
         * Methods
         *
        */

        public RestaurantId( string value ) : base( value ) {
            if( isEmpty() ) {
                throw new InvalidRestaurantId( value );
            }
        }

    }

}