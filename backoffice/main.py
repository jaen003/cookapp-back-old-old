"""
 *
 * Libraries 
 *
"""

from flask import Flask

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
    server.run( debug = True, host = '0.0.0.0' )

main() # call the main method