FETCH_SONG = """
    SELECT * FROM song SO
    WHERE 1 = 1
"""

def fetch_all_song(args):
    if args is None:
        query = FETCH_SONG
    
    return query