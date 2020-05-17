from flask import Flask, render_template
from model import db
import random


app = Flask(__name__)

@app.route("/")
def home():
    dbsize = len(db)
    max_db_index = dbsize - 1 
    index = random.randint(0,max_db_index)
    suggestion = db[index]
    return render_template(
        "home.html",
        suggestion = suggestion,
        index = index,
        dbsize = dbsize,
        max_db_index = max_db_index
    )