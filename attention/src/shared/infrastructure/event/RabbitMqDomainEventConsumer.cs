/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;
using attention.src.shared.domain;
using RabbitMQ.Client.Events;
using System.Text;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class RabbitMqDomainEventConsumer : DomainEventConsumer {

        /* 
         * 
         * Attributes
         *
        */

        private EventBusConnection          _busConnection;
        private DomainEventsInformation     _eventsInformation;
        private DomainEventJsonDeserializer _jsonDeserializer;

        /* 
         * 
         * Methods
         *
        */

        public RabbitMqDomainEventConsumer(
            EventBusConnection          busConnection,
            DomainEventsInformation     eventsInformation,
            DomainEventJsonDeserializer jsonDeserializer
        ) {
            _busConnection     = busConnection;
            _eventsInformation = eventsInformation;
            _jsonDeserializer  = jsonDeserializer;
        }

        public Task consume() {
            // Variables
            string eventName;
            string queueName;
            // code
            foreach( var eventInformation in _eventsInformation.all() ) {
                eventName      = eventInformation.eventName();
                queueName      = eventInformation.formatRabbitMqQueueName();
                consumeMessage( queueName, eventName, eventInformation.typeOfSubscribers() );
            }
            return Task.CompletedTask;
        }

        public void consumeMessage( 
            string     queueName, 
            string     eventName,
            List<Type> typeOfSubscribers
        ) {
            // Variables
            IModel                 channel;
            EventingBasicConsumer  consumer;
            DomainEventSubscriber? subscriber;
            DomainEvent?           domainEvent;
            // code
            channel = _busConnection.channel();
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
            consumer = new EventingBasicConsumer( channel );
            consumer.Received += async ( model, ea ) => {
                // Variables
                string message;
                byte[] body;
                // Code
                body            = ea.Body.ToArray();
                message         = Encoding.UTF8.GetString( body );
                Console.WriteLine( "message : {0}", message );
                domainEvent = _jsonDeserializer.deserialize( message );
                if( domainEvent != null ) {
                    foreach( Type subscriberType in typeOfSubscribers ) {
                        subscriber = ( DomainEventSubscriber? )Activator.CreateInstance( 
                            subscriberType 
                        );
                        if( subscriber != null ) {
                            await subscriber.handle( domainEvent );
                        }
                    }
                    channel.BasicAck( ea.DeliveryTag, false );
                }
            };
            channel.BasicConsume(
                queue    : queueName,
                autoAck  : false,
                consumer : consumer
            );
        }

    }

}
