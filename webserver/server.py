#!/usr/bin/env python
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

import application.index_insert




DATABASEURI = "postgresql://yz3917:1755@35.211.155.104/proj1part2"

#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")

# start the connection
@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
    print("******************** connection to psql is successful!! ********************")
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

# close the connection
@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
    print("******************** connection to psql is closed!! ********************")
  except Exception as e:
    pass

@app.route('/')
def index():
  # DEBUG: this is debugging code to see what request looks like
  print('*********************************************** request.args:', request.args)
  #
  # example of a database query
  #
  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = names)
  return render_template("index.html", **context)


@app.route('/another')
def another():
  return render_template("another.html")


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  
  query = application.index_insert.add_one_scientist(request.form)
  g.conn.execute(query)
  
  return redirect('/')


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    # debug=True makes it possible to dynamically show the changes in frontend to the webpages
    app.run(host=HOST, port=PORT, debug=True, threaded=threaded)

  run()
