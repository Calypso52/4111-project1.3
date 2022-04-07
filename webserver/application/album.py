import logging

FETCH_alb = """
SELECT a.album_id, a.name as album_name, a.release_time, a.popularity, ar.name as artist_name 
FROM album a join artist.ar on a.artist_id = ar.artist_id
"""

INSERT = """INSERT INTO album VALUES('{album_id}', '{name}', '{release_time}', {popularity}, '{artist_id}')"""

DELETE_ALBUM = """
    DELETE FROM album al WHERE al.name = '{name}'
"""

queryMap = {
    "album_id": " AND al.listener_id IN ({})",
    "name": " AND lower(al.name) LIKE lower('%%{}%%')",
    "release_time": " AND lower(al.release_time) = lower('{}')",
    "popularity": " AND al.popularity >= {}"
}

def fetch_all_album(args):
    query = FETCH_alb
    if args is not None:
        query += queryMap["name"].format(args['name']) if 'name' in args and len(args['name']) > 0 else ""
        query += queryMap["release_time"].format(args['release_time']) if 'release_time' in args and len(args['release_time']) > 0 else ""
        query += queryMap["popularity"].format(int(args['age'])) if 'age' in args and len(args['age']) > 0 else ""
    return query

def alb(alb_ref, args):
    add_alb = INSERT
    add_alb = add_alb.format(fda_id = str(int(alb_ref)), album_id = args['album_id'], name = args['name'], release_time = args['release_time'], popularity = args['popularity'], artist_id = args['artist_id'])
    return add_alb

def delete_al(args):
    delete_al = DELETE_ALBUM
    delete_al = delete_al.format(name = args["name"])
    return delete_al