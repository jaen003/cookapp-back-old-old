/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class DomainException : Exception {

        /* 
         * 
         * Constants
         *
        */

        public const int SERVER_INTERNAL_ERROR = 103;

        /* 
         * 
         * Attributes
         *
        */

        private int _code;

        /* 
         * 
         * Methods
         *
        */

        public DomainException( int code, string message ) : base( message ) {
            _code = code;
        }

        public int code() {
            return _code;
        }

    }

}