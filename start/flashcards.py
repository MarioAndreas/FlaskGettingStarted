from datetime import datetime
from flask import Flask

app = Flask(__name__)

count = 0
@app.route("/")
def welcome():
    global count
    count += 1
    return "Welcome to my Flash Cards application!"

@app.route("/date")
def date():
    global count
    count += 1
    return "This page was served at " + str(datetime.now())

@app.route("/counter")
def counter():
    global count
    count += 1
    return "Page Views:  " + str(count)