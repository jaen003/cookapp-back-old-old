/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;

/* 
 * 
 * Interfaces
 *
*/

namespace attention.src.shared.domain {

    public interface EventBusConnection {

        /* 
         * 
         * Methods
         *
        */

        IModel channel();

    }

}