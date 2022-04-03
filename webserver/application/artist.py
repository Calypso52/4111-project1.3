FETCH_ARTIST = """
    SELECT * FROM artist AR
    WHERE 1 = 1
"""

def fetch_all_artist(args):
    if args is None:
        query = FETCH_ARTIST
    
    return query