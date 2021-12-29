/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class ServerInternalError : DomainException {

        /* 
         * 
         * Methods
         *
        */

        public ServerInternalError() : base( 
            DomainException.SERVER_INTERNAL_ERROR,
            "Internal server error occurred while the request was being processed" 
        ) {
        }

    }

}