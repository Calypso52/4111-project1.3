FETCH_ALBUM = """
    SELECT * FROM album AL
    WHERE 1 = 1
"""

def fetch_all_albums(args):
    if args is None:
        query = FETCH_ALBUM
    
    return query