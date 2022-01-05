/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class InvalidRestaurantId : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_RESTAURANT_ID = 206;

        /* 
         * 
         * Methods
         *
        */

        public InvalidRestaurantId( string id ) : base( 
            INVALID_RESTAURANT_ID,
            string.Format( "The restaurant id {0} is invalid", id )
        ) {
        }

    }

}