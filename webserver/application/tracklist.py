FETCH_TRACKLIST = """
    SELECT * FROM tracklist TR
    WHERE 1 = 1
"""

def fetch_all_tracklist(args):
    if args is None:
        query = FETCH_TRACKLIST
    
    return query