"""
 *
 * Libraries 
 *
"""

from functools import wraps
from flask     import request

"""
 *
 * Methods 
 *
"""

def requestHttp( fields : list[str] ):
    def wrap( f ):
        @wraps( f )
        def decorated( *args, **kwargs ):
            # Variables
            data : dict
            ok   : bool
            # Code
            ok   = True
            data = request.json
            for field in fields:
                if not field in data:
                    ok = False
                    break
            if not ok:
                data = {}
            kwargs['data'] = data
            return f( *args, **kwargs )
        return decorated
    return wrap