/* 
 * 
 * Libraries
 *
*/

using attention.src.shared.domain;

/* 
 * 
 * Interfaces
 *
*/

namespace attention.src.table.domain {

    public interface TableRepository {

        /* 
         * 
         * Methods
         *
        */

        bool insert( Table table );
        bool update( Table table );
        Table? findById( TableId id );


    }

}