"""
 *
 * Libraries 
 *
"""

from flask                      import Flask
from app.product.infrastructure import exposeProductEntryPoints
from app.table.infrastructure   import exposeTableEntryPoints
from app.user.infrastructure    import exposeUserEntryPoints

"""
 *
 * Global variables 
 *
"""

server = Flask( __name__ )

"""
 *
 * Methods 
 *
"""

def exposeEntryPoints() -> None:
    exposeProductEntryPoints( server )
    exposeTableEntryPoints( server )
    exposeUserEntryPoints( server )

def main() -> None:
    exposeEntryPoints()
    server.run( debug = True, host = '0.0.0.0' )

main() # call the main method