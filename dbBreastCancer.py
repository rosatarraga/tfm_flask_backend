import json
from pymongo import MongoClient
from datetime import date
from bson.json_util import dumps

cluster = MongoClient("mongodb+srv://rosa:rosa@breastcancer.km0f51s.mongodb.net/?retryWrites=true&w=majority")

db = cluster["breastcancer"]
collection = db["logs"]

def createLog(email, patientID, benign_malign, view):
    print('creating log')
    collection.insert_one({"email":email, "date": date.today().strftime("%d/%m/%Y"), "patientID": patientID, "view":view, "score": benign_malign})

def returnEntries(email):
    cursor = collection.find( { "email": email } , {"date": 1, "patientID": 1, "score":1, "_id": 0})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    print (json_data)
    return json_data