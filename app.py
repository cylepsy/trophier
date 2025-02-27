import os

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass


app = Flask(__name__)

prefix = 'sqlite:///'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)

@dataclass
class Song(db.Model):
  id:int = db.Column(db.Integer, primary_key=True)
  title:str = db.Column(db.String(30))
  artist:str = db.Column(db.String(30))
  instrument:str = db.Column(db.String(10))
  type:str = db.Column(db.String(20))
  genre:str = db.Column(db.String(10))
  tag1:str = db.Column(db.String(10))


@dataclass
class TrophyData(db.Model):
  id:int = db.Column(db.Integer, primary_key=True)
  name:str = db.Column(db.String(30))
  rank:int = db.Column(db.Integer)
  description:str = db.Column(db.Text)

@dataclass
class TrophyEntry(db.Model):
  id:int = db.Column(db.Integer, primary_key=True)
  songid:int = db.Column(db.Integer)
  trophyid:int = db.Column(db.Integer)
  date = db.Column(db.Date)
  progress:str = db.Column(db.Integer)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Songs', methods=['GET'])
def all_songs():
  songs = Song.query.all()
  return jsonify({
    'status': 'success',
    'result': songs
  })

@app.route('/Trophies', methods=['GET'])
def all_trophies():
  trophies = TrophyData.query.all()
  return jsonify({
    'status': 'success',
    'result': trophies
  })

@app.route('/Addtrophy', methods=['POST'])
def add_trophy():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        tro = TrophyData(
            name = post_data.get('name'),
            rank = post_data.get('rank'),
            description = post_data.get('desc')
        )
        db.session.add(tro)
        db.session.commit()
        response_object['message'] = 'Trophy added!'
    return jsonify(response_object)

@app.route('/Addsong', methods=['POST'])
def add_song():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        song = Song(
            title = post_data.get('title'),
            artist = post_data.get('artist'),
            instrument = post_data.get('instrument'),
            type = post_data.get('type'),
            genre = post_data.get('genre'),
            tag1 = post_data.get('tag1'),
        )
        db.session.add(song)
        db.session.commit()
        response_object['message'] = 'Song added!'
    return jsonify(response_object)

@app.route('/querysong', methods=['POST'])
def query_song():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        id = post_data.get('songid')
        songQuery = TrophyEntry.query.filter_by(songid = id).all()
        return jsonify({
          'status': 'success',
          'result': songQuery
        })
