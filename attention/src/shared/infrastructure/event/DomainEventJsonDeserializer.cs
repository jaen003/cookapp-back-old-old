/* 
 * 
 * Libraries
 *
*/

using attention.src.shared.domain;
using Newtonsoft.Json;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class DomainEventJsonDeserializer {

        /* 
         * 
         * Attributes
         *
        */

        private DomainEventsInformation _eventsInformation;

        /* 
         * 
         * Methods
         *
        */

        public DomainEventJsonDeserializer( DomainEventsInformation eventsInformation ) {
            _eventsInformation = eventsInformation;
        }

        public DomainEvent? deserialize( string message ) {
            // Variables
            Dictionary<string, object>? data;
            Dictionary<string, string>? attributes;
            string                      eventName;
            DomainEventInformation?     eventInformation;
            Type                        eventType;
            DomainEvent?                instance;
            string?                     serializedAttributes;
            DomainEvent?                domainEvent;           
            // Code
            data = JsonConvert.DeserializeObject<Dictionary<string, object>>( message );
            if( data == null ) {
                return null;
            }
            serializedAttributes = data["attributes"].ToString();            
            attributes = JsonConvert.DeserializeObject<Dictionary<string, string>>( 
                serializedAttributes != null ? serializedAttributes : ""
            );      
            if( attributes == null ) {
                return null;
            }      
            eventName        = ( string )data["name"];
            eventInformation = _eventsInformation.findByName( eventName );
            if( eventInformation == null ) {
                return null;
            }
            eventType = eventInformation.eventType();            
            instance  = ( DomainEvent? )Activator.CreateInstance( eventType );
            if( instance == null ) {
                return null;
            }
            domainEvent = ( DomainEvent )instance.fromPrimitives( 
                eventId    : ( string )data["id"], 
                timestamp  : Int32.Parse( "" + data["timestamp"] ),
                attributes : attributes
            );
            return domainEvent;
        }

    }

}