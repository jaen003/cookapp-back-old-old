/* 
 * 
 * Interfaces
 *
*/

namespace attention.src.shared.domain {

    public interface EventBus {

        /* 
         * 
         * Methods
         *
        */

        Task publish( List<DomainEvent> events );

    }

}