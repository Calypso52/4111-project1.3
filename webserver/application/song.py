FETCH_SONG = """
    SELECT 
        S.song_id,
        S.name,
        S.popularity,
        S.dancibility,
        S.energy,
        S.speechiness,
        S.liveness,
        S.tempo,
        A.name
    FROM 
        song S,
        artist A
    WHERE
        S.artist_id = A.artist_id
"""

def fetch_all_song(args):
    if args is None:
        query = FETCH_SONG
    
    return query