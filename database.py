# database.py

from pymongo import MongoClient
from config import config

def get_notes_collection():
    client = MongoClient(config['MONGODB_URI'])
    db = client.get_default_database()
    return db['notes']

def fetch_notes_from_database(class_number):
    collection = get_notes_collection()
    note = collection.find_one({'class_number': class_number})
    return note['notes'] if note else None
