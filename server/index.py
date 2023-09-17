from flask import Flask, request, jsonify

from db import Database
app = Flask(__name__)
db=Database(app)


@app.route('/api/location', methods=["POST"])
def locationInfoApi():
    state = request.json['state']
    print("state",state)
    return state