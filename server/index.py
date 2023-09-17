from flask import Flask, request
from flask_cors import CORS
from db import Database
app = Flask(__name__)
cors = CORS(app)
db=Database(app)


@app.route('/api/location', methods=["POST"])
def locationInfoApi():
    print(request.get_data())
    state = str(request.get_data())
    res = db.getEntry(state)
    return res
# if __name__ == '__main__':
#     app.run(debug=True,port=5000)
