import json

def load_db():
    with open("suggestions-db.json") as f:
        return json.load(f)

db = load_db()    