/* 
 * 
 * Libraries 
 *
*/

using attention.src.table.domain;
using attention.src.shared.domain;
using attention.src.table.application;
using attention.src.table.infrastructure;

/* 
 * 
 * Classes 
 *
*/

namespace attention.app.eventHandler {

    public class TableCreatedEventHandler : DomainEventSubscriber {

        /* 
         * 
         * Methods
         *
        */

        public Type subscribedTo() {
            return typeof( TableCreated );
        }

        public Task handle( DomainEvent domainEvent ) => Task.Run(() => {
            // Variables
            TableCreated tableCreated;
            TableCreator creator;
            // Code
            tableCreated = ( TableCreated )domainEvent;
            creator      = new TableCreator( 
                repository : new TableMysqlRepository() 
            );
            creator.create(
                id           : new TableId( tableCreated.id() ),
                number       : new TableNumber( tableCreated.number() ),
                restaurantId : new RestaurantId( tableCreated.restaurantId() )
            );
        } );

    }

}