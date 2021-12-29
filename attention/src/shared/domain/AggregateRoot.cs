/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.domain {

    public class AggregateRoot {

        /* 
         * 
         * Attributes
         *
        */

        private List<DomainEvent> _events;

        /* 
         * 
         * Methods
         *
        */

        public AggregateRoot() {
            _events = new List<DomainEvent>();
        }

        public void record( DomainEvent domainEvent ) {
            _events.Add( domainEvent );
        }

        public List<DomainEvent> pullEvents() {
            // Variables
            List<DomainEvent> events;
            // Code
            events  = _events;
            _events = new List<DomainEvent>();
            return events;
        }

    }

}