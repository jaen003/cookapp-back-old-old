"""
 *
 * Libraries 
 *
"""

import os
import json
import time
from threading                         import Thread
from src.shared.domain                 import EventBus as Bus
from src.shared.domain                 import DomainEvent
from src.shared.domain                 import DomainEventSubscriber
from pika.adapters.blocking_connection import BlockingChannel
from pika                              import URLParameters
from pika                              import BlockingConnection

"""
 *
 * Classes 
 *
"""

class Singleton( type ):

    """
     *
     * Parameters 
     *
    """

    __instances = {}

    """
     *
     * Methods 
     *
    """

    def __call__( cls, *args, **kwargs ):
        if cls not in cls.__instances:
            instance = super().__call__( *args, **kwargs )
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class EventBus( Bus, metaclass = Singleton ):

    """
     *
     * Parameters 
     *
    """

    __topics : dict[ list[ DomainEventSubscriber ] ]

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> None:
        self.__topics = {}

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
    
    def __notify( self, event : DomainEvent ):
        # Variables
        subscribers : list[ DomainEventSubscriber ]
        topic       : str
        # Code
        self        = EventBus()
        topic       = event.topic()
        subscribers = self.__topics[topic]
        for subscriber in subscribers:
            subscriber.notify( event )
    
    def __callback( 
        self, 
        channel : BlockingChannel, 
        method, 
        body    : str, 
        event   : DomainEvent,
    ):
        message = json.loads( body )
        event.fromPrimitives( message )
        self.__notify( event )
        channel.basic_ack( delivery_tag = method.delivery_tag, multiple = False )
    
    def __consume( self, event : DomainEvent, queue : str ) -> None:
        # Variables
        channel    : BlockingChannel
        connection : BlockingConnection
        # Code
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
            on_message_callback = lambda ch, method, properties, body: 
                self.__callback( ch, method, body, event )
        )
        Thread( target = channel.start_consuming ).start()
    
    def subscribe( self, event : DomainEvent, subscriber : DomainEventSubscriber ) -> None:
        # Variables
        queue : str
        topic : str
        # Code
        topic = event.topic()
        queue = subscriber.subscribedTo()
        if topic in self.__topics:
            self.__topics[topic].append( subscriber )
        else:
            self.__topics[topic] = [subscriber]            
            self.__consume( event, queue )
            #Listener( event, queue )
            
class Listener( Thread ):

    """
     *
     * Parameters 
     *
    """

    __event   : DomainEvent
    __queue   : str
    __channel : BlockingChannel

    """
     *
     * Methods 
     *
    """

    def __init__( self, event : DomainEvent, queue : str ):
        Thread.__init__( self )
        self.__event = event
        self.__queue = queue
        self.__consume()

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
    
    def __callback( self, channel, method, properties, body ):
        message = json.loads( body )
        self.__event.fromPrimitives( message )
        EventBus.notify( self.__event )
        channel.basic_ack( delivery_tag = method.delivery_tag )

    def __consume( self ) -> None:
        connection     = self.__connect()
        self.__channel = connection.channel()
        self.__channel.exchange_declare(
            exchange      = self.__event.topic(),
            exchange_type = 'topic',
            durable       = True,
        )
        self.__channel.queue_declare(
            queue   = self.__queue,
            durable = True,       
        )
        self.__channel.queue_bind(
            queue       = self.__queue,
            exchange    = self.__event.topic(),
            routing_key = "#",
        )
        Thread( target = self.__channel.basic_consume(
            queue               = self.__queue, 
            on_message_callback = self.__callback,
        )  )
        self.start()
    
    def run( self ):
        self.__channel.start_consuming()

    


