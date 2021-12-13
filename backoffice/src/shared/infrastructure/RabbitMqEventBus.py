"""
 *
 * Libraries 
 *
"""

import os
import json
from threading                         import Thread
from src.shared.domain                 import EventBus
from src.shared.domain                 import DomainEvent
from pika.adapters.blocking_connection import BlockingChannel
from pika                              import URLParameters
from pika                              import BlockingConnection

"""
 *
 * Classes 
 *
"""

class RabbitMqEventBus( EventBus ):

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        pass

    def __connect( self ):
        # Variables
        user     : str
        password : str
        host     : str
        port     : str
        dsn      : str
        # Code
        password   = os.getenv( 'RABBITMQ_PASSWORD' )
        user       = os.getenv( 'RABBITMQ_USER' )
        port       = os.getenv( 'RABBITMQ_PORT' )
        host       = os.getenv( 'RABBITMQ_HOST' )
        dsn        = 'amqp://{}:{}@{}:{}/'.format( user, password, host, port )
        connection = BlockingConnection( URLParameters( dsn ) )
        return connection

    def publish( self, events : list[ DomainEvent ] ) -> None:
        # Variables
        channel    : BlockingChannel
        connection : BlockingConnection
        # Code
        connection = self.__connect()
        channel    = connection.channel()
        for event in events:
            channel.exchange_declare(
                exchange      = event.topic(),
                exchange_type = 'topic',
                durable       = True,
            )
            channel.basic_publish(
                exchange    = event.topic(), 
                routing_key = 'america.colombia',
                body        = json.dumps( event.body() ),
            )
        connection.close()
    
    def __callback( 
        self, 
        channel  : BlockingChannel, 
        method, 
        body     : str, 
        event    : DomainEvent,
        subscriber
    ):
        message = json.loads( body )
        event.fromPrimitives( message )
        subscriber( event )
        channel.basic_ack( delivery_tag = method.delivery_tag, multiple = False )
    
    def subscribe( self, event : DomainEvent, subscriber ) -> None:
        # Variables
        queue      : str
        topic      : str
        channel    : BlockingChannel
        connection : BlockingConnection
        # Code
        topic      = event.topic()
        queue      = 'backoffice_{}'.format( topic )
        connection = self.__connect()
        channel    = connection.channel()
        channel.exchange_declare(
            exchange      = event.topic(),
            exchange_type = 'topic',
            durable       = True,
        )
        channel.queue_declare(
            queue   = queue,
            durable = True,       
        )
        channel.queue_bind(
            queue       = queue,
            exchange    = event.topic(),
            routing_key = "#",
        )
        channel.basic_consume(
            queue               = queue,
            on_message_callback = lambda ch, method, _, body: 
                self.__callback( ch, method, body, event, subscriber )
        )
        Thread( target = channel.start_consuming ).start()         