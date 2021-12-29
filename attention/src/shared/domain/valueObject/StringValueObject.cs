/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class StringValueObject {

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

        public StringValueObject( string value ) {
            _value = value;
        }

        public string value() {
            return _value;
        }

        public bool isEmpty() {
            return _value == string.Empty;
        }

        public bool equals( StringValueObject value ) {
            return _value == value.value();
        }

    }

}