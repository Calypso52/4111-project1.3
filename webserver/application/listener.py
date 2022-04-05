FETCH_LISTENER = """
    SELECT * FROM listener LI
    WHERE 1 = 1
"""

INSERT_LISTENER = """
    INSERT INTO listener VALUES ('{listener_id}', '{name}', '{gender}', '{age}')
"""

DELETE_LISTENER = """
    DELETE FROM listener LI WHERE LI.name = '{name}'
"""

queryMap = {
    "listener_id": " AND LI.listener_id IN ({})",
    "name": " AND lower(LI.name) LIKE lower('%%{}%%')",
    "gender": " AND lower(LI.gender) = lower('{}')",
    "age": " AND LI.age >= {}"
}

def fetch_all_listener(args):
    query = FETCH_LISTENER
    if args is not None:
        query += queryMap["name"].format(args['name']) if 'name' in args and len(args['name']) > 0 else ""
        query += queryMap["gender"].format(args['gender']) if 'gender' in args and len(args['gender']) > 0 else ""
        query += queryMap["age"].format(int(args['age'])) if 'age' in args and len(args['age']) > 0 else ""
    
    return query

def add_listener(id, args):
    add_ls = INSERT_LISTENER
    add_ls = add_ls.format(listener_id = str(id), name = args["name"], gender = args["gender"], age = int(args["age"]))
    return add_ls

def delete_listener(args):
    delete_ls = DELETE_LISTENER
    delete_ls = delete_ls.format(name = args["name"])
    return delete_ls