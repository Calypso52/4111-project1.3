INSERT_ONE_ROW = """
    INSERT INTO test(name) VALUES ('{name}')
"""

def add_one_scientist(args):
    add_index = INSERT_ONE_ROW
    add_index = add_index.format(name = args['name'])
    return add_index