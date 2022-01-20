/* 
 * 
 * Libraries
 *
*/

using attention.src.shared.domain;

/* 
 * 
 * Classes 
 *
*/

namespace attention.src.table.domain {

    public class TableCreated : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private string _id;
        private int    _number;
        private string _restaurantId;

        /* 
         * 
         * Methods
         *
        */

        public TableCreated() {
            _id           = "";
            _number       = 0;
            _restaurantId = "";
        }

        public TableCreated(
            string  id,
            int     number,
            string  restaurantId
        ) {
            _id           = id;
            _number       = number;
            _restaurantId = restaurantId;
        }

        public TableCreated(
            string  id,
            int     number,
            string  restaurantId,
            string  eventId,
            int     timestamp
        ) : base( eventId, timestamp ) {
            _id           = id;
            _number       = number;
            _restaurantId = restaurantId;
        }

        public string id() {
            return _id;
        }

        public int number() {
            return _number;
        }

        public string restaurantId() {
            return _restaurantId;
        }

        public override string eventName() {
            return "table_created";
        }

        public override DomainEvent fromPrimitives( 
            string                    eventId, 
            int                       timestamp,
            Dictionary<string,string> attributes
        ) {
            // Variables
            TableCreated domainEvent;
            // Code
            domainEvent = new TableCreated(
                attributes["id"],
                Int32.Parse( attributes["number"] ),
                attributes["tableId"],
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override Dictionary<string, string> toPrimitives(){
            // Variables
            Dictionary<string, string> data;
            // Code
            data = new Dictionary<string, string>();
            data.Add( "id", _id );
            data.Add( "number", "" + _number );
            data.Add( "restaurantId", _restaurantId );
            return data;
        }
        
    }

}