/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class DomainEventsInformation {

        /* 
         * 
         * Attributes
         *
        */

        private List<DomainEventInformation> _eventsInformation;

        /* 
         * 
         * Methods
         *
        */

        public DomainEventsInformation( 
            List<DomainEventInformation> eventsInformation 
        ) {
            _eventsInformation = eventsInformation;
        }

        public List<DomainEventInformation> all() {
            return _eventsInformation;
        }

        public DomainEventInformation? findByName( string name ) {
            // Variables
            DomainEventInformation? response;
            // Code
            response = null;
            foreach( DomainEventInformation eventInformation in _eventsInformation ) {
                if( eventInformation.eventName() == name ) {
                    response = eventInformation;
                }
            }
            return response;
        }

    }
}
