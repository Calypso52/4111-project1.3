FETCH_ALBUM = """
    SELECT
        AL.album_id,
        AL.name,
        AL.release_time,
        AL.popularity,
        AR.name
    FROM 
        album AL,
        artist AR
    WHERE
        AL.artist_id = AR.artist_id
"""

def fetch_all_albums(args):
    if args is None:
        query = FETCH_ALBUM
    
    return query