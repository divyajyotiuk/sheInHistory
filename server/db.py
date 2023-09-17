from flask_pymongo import PyMongo
import urllib
from pymongo.server_api import ServerApi

class Database:
    def __init__(self,app):
        self.mongo_client= PyMongo(app, uri="mongodb+srv://gowdajotsna:"+urllib.parse.quote('Jotsna@080') + "@cluster0.eirnzcw.mongodb.net/shellh?retryWrites=true&w=majority",server_api=ServerApi('1'))
        self.db = self.mongo_client.db
    
    def addEntry(self, res):
        self.db.stateinfo.insert_one(res)

    def getEntry(self, state_name):
        print(state_name)
        return self.db.stateinfo.find_one({"state": state_name})


    
# def create_db_client(app):
#     mongo_client = PyMongo(app, uri="mongodb+srv://gowdajotsna:Jotsna@080@cluster0.eirnzcw.mongodb.net/")



