import logging

FETCH_alb = """
    SELECT 
        al.album_id, 
        al.name as album_name, 
        al.release_time, 
        al.popularity, 
        ar.name as artist_name 
    FROM album al, artist ar 
    where al.artist_id = ar.artist_id
"""

INSERT_ALBUM = """
    INSERT INTO album VALUES('{album_id}', '{name}', '{release_time}', {popularity}, '{artist_id}')
"""

DELETE_ALBUM = """
    DELETE FROM album al WHERE al.name = '{name}' AND al.artist_id = '{artist_id}'
"""

FETCH_ARTIST_NAME = """
    SELECT AR.artist_id FROM artist AR WHERE lower(AR.name) = lower('{}')
"""

queryMap = {
    "album_id": " AND al.album_id IN ({})",
    "name": " AND lower(al.name) LIKE lower('%%{}%%')",
    "release_time": " AND al.release_time > '{}'",
    "popularity": " AND al.popularity >= {}"
}

def fetch_all_album(args):
    query = FETCH_alb
    if args is not None:
        query += queryMap["name"].format(args['name']) if 'name' in args and len(args['name']) > 0 else ""
        query += queryMap["release_time"].format(args['release_time']) if 'release_time' in args and len(args['release_time']) > 0 else ""
        query += queryMap["popularity"].format(int(args['albumPopularity'])) if 'albumPopularity' in args and len(args['albumPopularity']) > 0 else ""
    return query

def fetch_artist_name(args):
    artist_id = FETCH_ARTIST_NAME
    artist_id = artist_id.format(args["artist"])
    return artist_id

def add_album(album_id, artist_id, args):
    add_album = INSERT_ALBUM
    add_album = add_album.format(album_id = str(album_id), name = args["name"], release_time = args["release_time"], popularity = args["albumPopularityAdd"], artist_id = artist_id)
    return add_album

def delete_album(artist_id, args):
    delete_album = DELETE_ALBUM
    delete_album = delete_album.format(name = args["name"], artist_id = artist_id)
    return delete_album