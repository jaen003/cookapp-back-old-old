/* 
 * 
 * Interfaces
 *
*/

namespace attention.src.shared.domain {

    public interface DomainEventSubscriber {

        /* 
         * 
         * Methods
         *
        */

        Task handle( DomainEvent domainEvent );

        Type subscribedTo();

    }

}