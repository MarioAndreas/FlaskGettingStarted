# Flask Notes

## First Basic example
- import flask
- routes
- function that generates content
### Code example:
```python
    from flask import Flask
    from datetime import datetime

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
```

## `from flask import Flask`
Import the flask class

## `app = Flask(__name__)`
Create a flask instance with the name of the module (filename)  
Save it in the `app` variable

## `@app.route("/")`
Decorator: has the URL path  
"/" would be the root or home page - http://domain.com/  
`@app.route("/date")`  URL for /date page - http://domain.com/date  
The function under this decorator defines the contents of that page.  

## `def welcome():`
The function that defines the contents of that page.    
The `return` statement returns the content.  

---
## Running the App
### Set the environment variables
```
set FLASK_APP=flashcards.py
set FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` to `development` allows flask to produce verbose error messages.  
`flask run` will start the app set in `FLASK_APP`  
