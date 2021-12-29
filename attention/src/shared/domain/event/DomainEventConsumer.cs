/* 
 * 
 * Interfaces
 *
*/

namespace attention.src.shared.domain {

    public interface DomainEventConsumer {

        /* 
         * 
         * Methods
         *
        */
        
        Task consume();

    }

}