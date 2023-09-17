from flask import Flask, request
from flask_cors import CORS
from db import Database
import json

app = Flask(__name__)
cors = CORS(app)
db=Database(app)

@app.route('/api/location', methods=["POST"])
def locationInfoApi():
    print(request.get_data())
    parsed_data = json.loads(request.get_data())
    res = db.getEntry(parsed_data['state'])
    return res
# if __name__ == '__main__':
#     app.run(debug=True,port=5000)
