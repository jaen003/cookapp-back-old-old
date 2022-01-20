/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public abstract class DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private string _eventId;
        private int    _timestamp;

        /* 
         * 
         * Methods
         *
        */

        public DomainEvent( string eventId, int timestamp ) {
            _eventId   = eventId;
            _timestamp = timestamp;
        }

        public DomainEvent() {
            _eventId   = generateId();
            _timestamp = getTimestamp();
        }

        private string generateId() {
            // Variables
            Guid guid;
            // Code
            guid = Guid.NewGuid();
            return guid.ToString();
        }

        private int getTimestamp() {
            // Variables
            DateTime now;
            int      timestamp;
            // Code
            now       = DateTime.UtcNow;
            timestamp = ( int )( now.Subtract( new DateTime( 1970, 1, 1 ) ) ).TotalSeconds;
            return timestamp;
        }

        public string eventId() {
            return _eventId;
        }

        public int timestamp() {
            return _timestamp;
        }

        public abstract string eventName();

        public abstract Dictionary<string,string> toPrimitives();

        public abstract DomainEvent fromPrimitives( 
            string                    eventId, 
            int                       timestamp,
            Dictionary<string,string> attributes
        );

    }

}