FETCH_LISTENER = """
    SELECT * FROM listener LI
    WHERE 1 = 1
"""

def fetch_all_listener(args):
    if args is None:
        query = FETCH_LISTENER
    
    return query