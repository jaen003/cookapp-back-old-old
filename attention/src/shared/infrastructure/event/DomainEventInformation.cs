/* 
 * 
 * Libraries
 *
*/

using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class DomainEventInformation {

        /* 
         * 
         * Attributes
         *
        */

        private List<Type> _typeOfSubscribers;
        private Type       _eventType;

        /* 
         * 
         * Methods
         *
        */

        public DomainEventInformation( 
            Type       eventType, 
            List<Type> typeOfSubscribers
        ) {
            _typeOfSubscribers = typeOfSubscribers;
            _eventType         = eventType;
        }

        public string eventName() {
            // Variables
            DomainEvent? domainEvent;
            string       eventName;
            // Code
            domainEvent = ( DomainEvent? )Activator.CreateInstance( _eventType );
            eventName   = domainEvent != null ? domainEvent.eventName() : "";
            return eventName;
        }

        public string formatRabbitMqQueueName() {
            return string.Format( "attention_{0}", eventName() );
        }

        public List<Type> typeOfSubscribers() {
            return _typeOfSubscribers;
        }

        public Type eventType() {
            return _eventType;
        }

    }
}
