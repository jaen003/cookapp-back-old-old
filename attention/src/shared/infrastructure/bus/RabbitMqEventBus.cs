/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;
using attention.src.shared.domain;
using System.Text;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class RabbitMqEventBus : EventBus {

        /* 
         * 
         * Attributes
         *
        */

        private EventBusConnection _busConnection;

        /* 
         * 
         * Methods
         *
        */

        public RabbitMqEventBus( EventBusConnection busConnection ) {
            _busConnection = busConnection;
        }

        public async Task publish( List<DomainEvent> events ) {
            await Task.Run( () => {
                foreach( DomainEvent domainEvent in events ) {
                    publishEvent( domainEvent );
                }
            } );
        }

        private void publishEvent( DomainEvent domainEvent ) {
            // Variables
            IModel channel;
            string message;
            byte[] body;
            // Code
            message = DomainEventJsonSerializer.serialize( domainEvent );
            body    = UTF8Encoding.UTF8.GetBytes( message );
            channel = _busConnection.channel();
            channel.ExchangeDeclare(
                exchange: domainEvent.eventName(),
                type: "topic",
                durable: true
            );
            channel.BasicPublish(
                exchange: domainEvent.eventName(),
                routingKey: "america.colombia",
                basicProperties: null,
                body: body
            );
            channel.Close();    
        }

    }

}