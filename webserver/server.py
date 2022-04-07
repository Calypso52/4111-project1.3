#!/usr/bin/env python
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
import uuid

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# python files
import application.index_insert
import application.album
import application.artist
import application.listener
import application.song
import application.tracklist

DATABASEURI = "postgresql://yz3917:1755@35.211.155.104/proj1part2"

# This line creates a database engine that knows how to connect to the URI above.
engine = create_engine(DATABASEURI)

# start the connection
@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

# close the connection
@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def index():
  return render_template("index.html")


# route to album interface
@app.route('/album')
def album():
  return render_template("album/album.html")

# search router of the album interface
@app.route('/album/<searchContent>')
def album_search_content(searchContent):
  # store query result array
  result = []
  
  ########################################### get all data of album ###########################################
  if searchContent == 'all':
    rows = ['album_id', 'name', 'release_time', 'popularity', 'artist_name']
    query = application.album.fetch_all_albums(None)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
  
  return render_template("album/albumAll.html", **dict(data = result))


# route to artist interface
@app.route('/artist')
def artist():
  return render_template("artist/artist.html")


# search router of the artist interface
@app.route('/artist/<searchContent>', methods=["POST", "GET"])
def artist_search_content(searchContent):
  # store query result array
  result = []
  
  if searchContent == 'all':
    rows = ['artist_id', 'name', 'gender', 'popularity', 'genre', 'follower']
    query = application.artist.fetch_all_artist(None)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("artist/artistAll.html", **dict(data = result))
  elif searchContent == 'find':
    print('form =', request.form)
    rows = ['artist_id', 'name', 'gender', 'popularity', 'genre', 'follower']
    query = application.artist.fetch_all_artist(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("artist/artistAll.html", **dict(data = result))
  elif searchContent == 'add':
    print('form =', request.form)
    query = application.artist.add_artist(uuid.uuid1(), request.form)
    cursor = g.conn.execute(query)
    return redirect("/artist")
  elif searchContent == 'delete':
    print('form =', request.form)
    query = application.artist.delete_artist(request.form)
    cursor = g.conn.execute(query)
    return redirect("/artist")
  elif searchContent == "mostPopularMale" or searchContent == "mostPopularFemale":
    rows = ['artist_id', 'name', 'gender', 'popularity', 'genre', 'follower']
    gender = 'M' if searchContent == "mostPopularMale" else 'F'
    query = application.artist.FETCH__popularart(gender)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("artist/artistAll.html", **dict(data = result))
  elif searchContent == "mostFollowerMale" or searchContent == "mostFollowerFemale":
    rows = ['artist_id', 'name', 'gender', 'popularity', 'genre', 'follower']
    gender = 'M' if searchContent == "mostFollowerMale" else 'F'
    query = application.artist.FETCH__followerart(gender)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("artist/artistAll.html", **dict(data = result))

# route to listener interface
@app.route('/listener')
def listener():
  return render_template("listener/listener.html")


# search router of the listener interface
@app.route('/listener/<searchContent>', methods=["POST", "GET"])
def listener_search_content(searchContent):
  # store query result array
  result = []
  
  if searchContent == 'all':
    rows = ['listener_id', 'name', 'gender', 'age']
    query = application.listener.fetch_all_listener(None)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("listener/listenerAll.html", **dict(data = result))
  elif searchContent == 'add':
    print('form =', request.form)
    query = application.listener.add_listener(uuid.uuid1(), request.form)
    cursor = g.conn.execute(query)
    return redirect("/listener")
  elif searchContent == 'find':
    print('form =', request.form)
    rows = ['listener_id', 'name', 'gender', 'age']
    query = application.listener.fetch_all_listener(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("listener/listenerAll.html", **dict(data = result))
  elif searchContent == 'delete':
    print('form =', request.form)
    query = application.listener.delete_listener(request.form)
    cursor = g.conn.execute(query)
    return redirect("/listener")
  
  
# route to song interface
@app.route('/song')
def song():
  return render_template("song/song.html")


# search router of the song interface
@app.route('/song/<searchContent>', methods=["POST", "GET"])
def song_search_content(searchContent):
  # store query result array
  result = []
  
  if searchContent == 'all':
    rows = ['song_id', 'name', 'popularity', 'dancibility', 'energy', 'speechiness', 'liveness', 'tempo', 'artist_name']
    query = application.song.fetch_all_song(None)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("song/songAll.html", **dict(data = result))
  elif searchContent == 'find':
    print('form =', request.form)
    rows = ['song_id', 'name', 'popularity', 'dancibility', 'energy', 'speechiness', 'liveness', 'tempo', 'artist_name']
    query = application.song.fetch_all_song(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("song/songAll.html", **dict(data = result))
  elif searchContent == 'add':
    print('form =', request.form)
    # get creator name
    rows = ['artist_id']
    query = application.song.fetch_artist_name(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    if len(result) > 0:
      print('bingo_artist_id =', result[0]["artist_id"])
      bingo_artist_id = result[0]["artist_id"]
      query = application.song.add_song(uuid.uuid1(), bingo_artist_id, request.form)
      cursor = g.conn.execute(query)
    return redirect("/song")
  elif searchContent == 'delete':
    print('form =', request.form)
    # get creator name
    rows = ['artist_id']
    query = application.song.fetch_artist_name(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    if len(result) > 0:
      print('bingo_artist_id =', result[0]["artist_id"])
      bingo_artist_id = result[0]["artist_id"]
      query = application.song.delete_song(bingo_artist_id, request.form)
      cursor = g.conn.execute(query)
    return redirect("/song")
  else:
    rows = ['song_id', 'name', 'popularity', 'dancibility', 'energy', 'speechiness', 'liveness', 'tempo', 'artist_name']
    query = application.song.FETCH__trending_song(searchContent)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("song/songAll.html", **dict(data = result))


# route to tracklist interface
@app.route('/tracklist')
def tracklist():
  return render_template("tracklist/tracklist.html")


# search router of the tracklist interface
@app.route('/tracklist/<searchContent>', methods=["POST", "GET"])
def tracklist_search_content(searchContent):
  # store query result array
  result = []
  
  if searchContent == 'all':
    rows = ['list_id', 'name', 'popularity', 'create_listener_name']
    query = application.tracklist.fetch_all_tracklist(None)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("tracklist/tracklistAll.html", **dict(data = result))
  elif searchContent == 'find':
    print('form =', request.form)
    rows = ['list_id', 'name', 'popularity', 'create_listener_name']
    query = application.tracklist.fetch_all_tracklist(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("tracklist/tracklistAll.html", **dict(data = result))
  elif searchContent == 'add':
    print('form =', request.form)
    # get creator name
    rows = ['listener_id']
    query = application.tracklist.fetch_creator_listener_name(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    if len(result) > 0:
      print('bingo_listener_id =', result[0]["listener_id"])
      bingo_listener_id = result[0]["listener_id"]
      query = application.tracklist.add_tracklist(uuid.uuid1(), bingo_listener_id, request.form)
      cursor = g.conn.execute(query)
    return redirect("/tracklist")
  elif searchContent == 'delete':
    print('form =', request.form)
    # get creator name
    rows = ['listener_id']
    query = application.tracklist.fetch_creator_listener_name(request.form)
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    if len(result) > 0:
      print('bingo_listener_id =', result[0]["listener_id"])
      bingo_listener_id = result[0]["listener_id"]
      query = application.tracklist.delete_tracklist(bingo_listener_id, request.form)
      cursor = g.conn.execute(query)
    return redirect("/tracklist")
  elif searchContent == 'mostPopular':
    rows = ['list_id', 'name', 'popularity', 'create_listener_name']
    query = application.tracklist.FETCH__popularlist()
    cursor = g.conn.execute(query)
    for item in cursor:
      result.append(dict(zip(rows, item)))
    return render_template("tracklist/tracklistAll.html", **dict(data = result))


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    # debug=True makes it possible to dynamically show the changes in frontend to the webpages
    app.run(host=HOST, port=PORT, debug=True, threaded=threaded)

  run()
