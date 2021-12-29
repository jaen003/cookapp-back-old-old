/* 
 * 
 * Libraries
 *
*/

using System.Reflection;
using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.shared.infrastructure {

    public static class DomainEventMapper {

        /* 
         * 
         * Methods
         *
        */

        public static IServiceCollection AddDomainEventInformation( 
            this IServiceCollection services
        ) {
            // Variables
            IEnumerable<TypeInfo>        classTypes;
            IEnumerable<TypeInfo>        interfaces;
            IEnumerable<TypeInfo>        subscribers;
            Dictionary<Type, List<Type>> eventsInformation;
            List<DomainEventInformation> information;
            List<Type>                   subscribersInformation;
            Assembly                     assembly;
            // Code
            eventsInformation = new Dictionary<Type, List<Type>>();
            assembly          = Assembly.Load( "attention" );
            classTypes        = assembly.ExportedTypes.Select(
                t => t.GetTypeInfo()
            ).Where( t => t.IsClass && !t.IsAbstract );
            foreach( TypeInfo type in classTypes ) {
                interfaces  = type.ImplementedInterfaces.Select( i => i.GetTypeInfo() );
                subscribers = interfaces.Where( i =>
                    i.AsType() == typeof( DomainEventSubscriber )
                );
                foreach( TypeInfo handlerInterfaceType in subscribers ) {
                    dynamic? subscriber;
                    subscriber = Activator.CreateInstance( type.AsType() );
                    Type domainEvent = subscriber != null ? subscriber.subscribedTo() : Type.EmptyTypes;
                    if( eventsInformation.ContainsKey( domainEvent ) ) {
                        subscribersInformation = eventsInformation[domainEvent];
                        subscribersInformation.Add( type.AsType() );
                    } else {
                        subscribersInformation = new List<Type>();
                        subscribersInformation.Add( type.AsType() );
                        eventsInformation.Add( domainEvent, subscribersInformation );
                    }
                } 
            }
            information = new List<DomainEventInformation>();
            foreach( KeyValuePair<Type, List<Type>> eventInformation in eventsInformation ) {
                information.Add( new DomainEventInformation(
                    eventInformation.Key, 
                    eventInformation.Value
                ) );
            }
            services.AddTransient( s => new DomainEventsInformation( information ) );
            return services;
        }

    }

}