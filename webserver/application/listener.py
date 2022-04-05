FETCH_LISTENER = """
    SELECT * FROM listener LI
    WHERE 1 = 1
"""

INSERT_LISTENER = """
    INSERT INTO listener VALUES ('{listener_id}', '{name}', '{gender}', '{age}')
"""

def fetch_all_listener(args):
    if args is None:
        query = FETCH_LISTENER
    
    return query

def add_listener(id, args):
    add_ls = INSERT_LISTENER
    add_ls = add_ls.format(listener_id = str(id), name = args["name"], gender = args["gender"], age = args["age"])
    print('query:', add_ls)
    return add_ls