/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class UuidValueObject {

        /* 
         * 
         * Attributes
         *
        */

        private string _value;

        /* 
         * 
         * Methods
         *
        */

        public UuidValueObject( string? value = null ) {
            if( value == null ) {
                value = generateValue();
            }
            _value = value;
        }

        private string generateValue() {
            // Variables
            Guid guid;
            // Code
            guid = Guid.NewGuid();
            return guid.ToString();
        }

        public string value() {
            return _value;
        }

        public bool isEmpty() {
            return _value == string.Empty;
        }

        public bool equals( UuidValueObject value ) {
            return _value == value.value();
        }

    }

}