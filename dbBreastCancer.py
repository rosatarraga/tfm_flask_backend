import pymongo
from pymongo import MongoClient
from datetime import date

cluster = MongoClient("mongodb+srv://rosa:rosa@breastcancer.km0f51s.mongodb.net/?retryWrites=true&w=majority")

db = cluster["breastcancer"]
collection = db["logs"]

def createLog(email, patient_id, benign_malign, view):
    print('creating log')
    collection.insert_one({"email":email, "date": date.today().strftime("%d/%m/%Y"), "patient_id": patient_id, "view":view, "benign_malign": benign_malign})

def returnEntries():
    return 'ok'