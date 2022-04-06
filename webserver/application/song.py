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

FETCH_ARTIST_NAME = """
    SELECT AR.artist_id FROM artist AR WHERE lower(AR.name) = lower('{}')
"""

INSERT_SONG = """
    INSERT INTO song VALUES('{song_id}', '{name}', '{popularity}', '{dancibility}', '{energy}', '{speechiness}', '{liveness}', '{tempo}', '{artist_id}')
"""

DELETE_SONG = """
    DELETE FROM song S WHERE S.name = '{name}' AND S.artist_id = '{artist_id}'
"""

queryMap = {
    "S.name": " AND lower(S.name) LIKE lower('%%{}%%')",
    "S.popularity": " AND S.popularity >= {}",
    "S.dancibility": " AND S.dancibility >= {}",
    "S.energy": " AND S.energy >= {}",
    "S.speechiness": " AND S.speechiness >= {}",
    "S.liveness": " AND S.liveness >= {}",
    "S.tempo": " AND S.tempo >= {}",
    "A.name": " AND lower(A.name) LIKE lower('%%{}%%')"
}

def fetch_all_song(args):
    query = FETCH_SONG
    if args is not None:
        query += queryMap["S.name"].format(args["name"]) if "name" in args and len(args["name"]) > 0 else ""
        query += queryMap["A.name"].format(args["artist"]) if "artist" in args and len(args["artist"]) > 0 else ""
        query += queryMap["S.popularity"].format(int(args["songPopularityFind"])) if "songPopularityFind" in args and len(args['songPopularityFind']) > 0 else ""
        query += queryMap["S.dancibility"].format(float(args["songDancibilityFind"])) if "songDancibilityFind" in args and len(args['songDancibilityFind']) > 0 else ""
        query += queryMap["S.energy"].format(float(args["songEnergyFind"])) if "songEnergyFind" in args and len(args['songEnergyFind']) > 0 else ""
        query += queryMap["S.speechiness"].format(float(args["songSpeechinessFind"])) if "songSpeechinessFind" in args and len(args['songSpeechinessFind']) > 0 else ""
        query += queryMap["S.liveness"].format(float(args["songLivenessFind"])) if "songLivenessFind" in args and len(args['songLivenessFind']) > 0 else ""
        query += queryMap["S.tempo"].format(float(args["songTempoFind"])) if "songTempoFind" in args and len(args['songTempoFind']) > 0 else ""
    
    return query

def fetch_artist_name(args):
    artist_id = FETCH_ARTIST_NAME
    artist_id = artist_id.format(args["artist"])
    return artist_id

def add_song(song_id, artist_id, args):
    add_song = INSERT_SONG
    add_song = add_song.format(song_id = str(song_id), 
                               name = args["name"], 
                               artist_id = artist_id, 
                               popularity = 0,
                               dancibility = 0,
                               energy = 0,
                               speechiness = 0,
                               liveness = 0,
                               tempo = 0)
    return add_song

def delete_song(artist_id, args):
    delete_song = DELETE_SONG
    delete_song = delete_song.format(name = args["name"], artist_id = artist_id)
    return delete_song