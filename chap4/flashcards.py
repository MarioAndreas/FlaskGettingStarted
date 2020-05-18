from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=db
    )

@app.route("/card")
@app.route("/card/<int:index>")
def card_view(index=0):
    max_index = len(db) - 1
    #if index > max_index:
        #index = 0
    #if index < 0:
        #index = max_index

    try:
        card = db[index]
        return render_template("card.html", 
                                card=card, 
                                index=index,
                                max_index=max_index)
    except IndexError:
        abort(404)

@app.route("/api/card")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)