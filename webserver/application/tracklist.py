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

INSERT_TRACKLIST = """
    INSERT INTO tracklist VALUES('{list_id}', '{name}', {popularity}, '{listener_id}')
"""

FETCH_CREATOR_LISTENER = """
    SELECT L.listener_id FROM listener L WHERE lower(L.name) = lower('{}')
"""

DELETE_TRACKLIST = """
    DELETE FROM tracklist TR WHERE TR.name = '{name}' AND TR.listener_id = '{listener_id}'
"""

queryMap = {
    "TR.list_id": " AND TR.list_id IN ({})",
    "TR.name": " AND lower(TR.name) LIKE lower('%%{}%%')",
    "LI.name": " AND lower(LI.name) LIKE lower('%%{}%%')",
    "TR.popularity": " AND TR.popularity >= {}"
}

def fetch_all_tracklist(args):
    query = FETCH_TRACKLIST
    if args is not None:
        query += queryMap["LI.name"].format(args["creator"]) if "creator" in args and len(args["creator"]) > 0 else ""
        query += queryMap["TR.name"].format(args["title"]) if "title" in args and len(args["title"]) > 0 else ""
        query += queryMap["TR.popularity"].format(int(args["popularity"])) if "popularity" in args and len(args['popularity']) > 0 else ""
    
    return query

def fetch_creator_listener_name(args):
    listener_id = FETCH_CREATOR_LISTENER
    listener_id = listener_id.format(args["creator"])
    return listener_id

def add_tracklist(tracklist_id, creator_listener_id, args):
    add_tr = INSERT_TRACKLIST
    add_tr = add_tr.format(list_id = str(tracklist_id), name = args["title"], popularity = int(args["popularity"]), listener_id = creator_listener_id)
    return add_tr

def delete_tracklist(bingo_listener_id, args):
    delete_tr = DELETE_TRACKLIST
    delete_tr = delete_tr.format(name = args["name"], listener_id = bingo_listener_id)
    return delete_tr