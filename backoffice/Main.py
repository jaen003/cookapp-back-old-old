"""
 *
 * Libraries 
 *
"""

from flask      import Flask
from flask_cors import CORS
from app        import exposeEntryPoints


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

def main() -> None:
    exposeEntryPoints( server )
    CORS( server, resources = { r"/api/*" : { "origins" : "*" } } )
    server.run( debug = False, host = '0.0.0.0' )

main() # call the main method