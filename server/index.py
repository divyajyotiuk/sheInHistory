from flask import Flask, request, jsonify
import json
from db import Database
app = Flask(__name__)
db=Database(app)


@app.route('/api/location', methods=["POST"])
def locationInfoApi():
    state = str(request.get_data()).split('=')[1][:-1]
    res = db.getEntry(state)
    return res
# if __name__ == '__main__':
#     app.run(debug=True,port=5000)