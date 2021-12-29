/* 
 * 
 * Libraries
 *
*/

using System.Collections.Generic;
using System.Linq;
using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class DomainEventJsonSerializer {

        /* 
         * 
         * Methods
         *
        */

        public static string serialize( DomainEvent domainEvent ) {
            // Variables
            Dictionary<string,string> attributes;
            string                    response;
            IEnumerable<string>       data;
            // Code
            attributes = domainEvent.toPrimitives();
            response   = "{ " + string.Format( 
                "\"id\":\"{0}\", \"name\":\"{1}\", \"timestamp\":{2}, ", 
                domainEvent.eventId(),
                domainEvent.eventName(),
                domainEvent.timestamp()
            );
            data = attributes.Select( attribute => 
                string.Format( "\"{0}\":\"{1}\"", attribute.Key, attribute.Value )
            );
            response += "\"attributes\":{ " + string.Join( ", ", data ) + " } }";
            return response;
        }

    }

}