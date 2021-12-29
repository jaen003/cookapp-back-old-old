/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;
using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class RabbitMqEventBusConfiguration : EventBusConfiguration {

        /* 
         * 
         * Attributes
         *
        */

        private EventBusConnection      _busConnection;
        private DomainEventsInformation _eventsInformation;

        /* 
         * 
         * Methods
         *
        */

        public RabbitMqEventBusConfiguration( 
            EventBusConnection      busConnection,
            DomainEventsInformation eventsInformation
        ) {
            _busConnection     = busConnection;
            _eventsInformation = eventsInformation;
        }

        public void configure() {
            // Variables
            IModel channel;
            string eventName;
            string queueName;
            // code
            channel = _busConnection.channel();
            foreach( var eventInformation in _eventsInformation.all() ) {
                eventName = eventInformation.eventName();
                channel.ExchangeDeclare(
                    exchange : eventName, 
                    type     : "topic", 
                    durable  : true
                );
                queueName = eventInformation.formatRabbitMqQueueName();
                channel.QueueDeclare(
                    queue      : queueName,
                    durable    : true,
                    exclusive  : false,
                    autoDelete : false
                );
                channel.QueueBind(
                    exchange   : eventName, 
                    queue      : queueName,
                    routingKey : "#"
                );
            }
            channel.Close();
        }

    }

}
