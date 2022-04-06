FETCH_ARTIST = """
    SELECT * FROM artist AR
    WHERE 1 = 1
"""

INSERT_ARTIST = """
    INSERT INTO artist VALUES('{artist_id}', '{name}', '{gender}', '{popularity}', '{genre}', '{follower}')
"""

DELETE_ARTIST = """
    DELETE FROM artist AR WHERE AR.name = '{name}'
"""

queryMap = {
    "artist_id": " AND AR.artist_id IN ({})",
    "name": " AND lower(AR.name) LIKE lower('%%{}%%')",
    "gender": " AND lower(AR.gender) = lower('{}')",
    "popularity": " AND AR.popularity >= {}",
    "genre": " AND lower(AR.genre) LIKE lower('%%{}%%')",
    "follower" : " AND AR.follower >= {}"
}

def fetch_all_artist(args):
    query = FETCH_ARTIST
    if args is not None:
        query += queryMap["name"].format(args["name"]) if 'name' in args and len(args['name']) > 0 else ""
        query += queryMap["gender"].format(args['gender']) if 'gender' in args and len(args['gender']) > 0 else ""
        query += queryMap["popularity"].format(int(args["artistPopularity"])) if 'artistPopularity' in args and len(args['artistPopularity']) > 0 else ""
        query += queryMap["genre"].format(args["genre"]) if 'genre' in args and args['genre'] != 'Select genre' else ""
        query += queryMap["follower"].format(args["artistFollower"]) if 'artistFollower' in args and len(args['artistFollower']) > 0 else ""
    
    return query

def add_artist(id, args):
    add_ar = INSERT_ARTIST
    add_ar = add_ar.format(artist_id = str(id), 
                           name = args["name"], 
                           gender = args["gender"], 
                           popularity = args["artistPopularityAdd"], 
                           genre = args["genre"], 
                           follower = args["artistFollowerAdd"])
    return add_ar

def delete_artist(args):
    delete_ar = DELETE_ARTIST
    delete_ar = delete_ar.format(name = args["name"])
    return delete_ar