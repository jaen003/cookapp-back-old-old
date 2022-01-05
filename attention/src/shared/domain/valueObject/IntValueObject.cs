/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class IntValueObject {

        /* 
         * 
         * Attributes
         *
        */

        private int _value;

        /* 
         * 
         * Methods
         *
        */

        public IntValueObject( int value ) {
            _value = value;
        }

        public int value() {
            return _value;
        }

        public bool equals( int value ) {
            return _value == value;
        }

        public bool isLessThan( int value ) {
            return _value < value;
        }

        public bool isBiggerThan( int value ) {
            return _value > value;
        }

        public string toString() {
            return _value.ToString();
        }

    }

}