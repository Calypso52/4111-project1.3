FETCH_TRACKLIST = """
    SELECT
        TR.list_id,
        TR.name,
        TR.popularity,
        LI.name
    FROM 
        tracklist TR,
        listener LI
    WHERE
        TR.listener_id = LI.listener_id
"""

def fetch_all_tracklist(args):
    if args is None:
        query = FETCH_TRACKLIST
    
    return query