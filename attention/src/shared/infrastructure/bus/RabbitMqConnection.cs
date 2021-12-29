/* 
 * 
 * Libraries
 *
*/

using attention.src.shared.domain;
using RabbitMQ.Client;
using RabbitMQ.Client.Exceptions;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public class RabbitMqConnection : EventBusConnection {

        /* 
         * 
         * Attributes
         *
        */

        private ConnectionFactory _connectionFactory;
        private IConnection?      _connection = null;
        private IModel?           _channel    = null;

        /* 
         * 
         * Methods
         *
        */

        public RabbitMqConnection() {
            // Variables
            string? user;
            string? password;
            string? host;
            string? port;
            string  rabbitUri;
            // Code
            user     = Environment.GetEnvironmentVariable( "RABBITMQ_USER" );
            password = Environment.GetEnvironmentVariable( "RABBITMQ_PASSWORD" );
            port     = Environment.GetEnvironmentVariable( "RABBITMQ_PORT" );
            host     = Environment.GetEnvironmentVariable( "RABBITMQ_HOST" );
            _connectionFactory = new ConnectionFactory();
            rabbitUri = string.Format( "amqp://{0}:{1}@{2}:{3}", user, password, host, port );
            _connectionFactory.Uri = new Uri( rabbitUri );
        }

        private IConnection connection() {
            while( _connection == null ) {
                try {
                    _connection = _connectionFactory.CreateConnection(); 
                } catch( BrokerUnreachableException ) {
                    Thread.Sleep( 1000 );
                }
            }
            return _connection;
        }

        public IModel channel() {
            return connection().CreateModel();
        }

    }

}
