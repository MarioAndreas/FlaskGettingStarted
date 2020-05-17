# Templates (Jinja) and Static files

## Templates
Jinja templates
- Display data to user
- Generates HTML
- The View function calls templates
- The View passes data to the template
- Data placed into Jinja variables in the template

Default directory name: 'templates'  
These files contain HTML with variables   
Variable content is denoted with: `{{ }}`  
Must import `render_template` from the `flask` module  

    from flask import Flask, render_template
    
The `render_template` function take the template file name as the first argument  
The rest of the args are variables that will be passed into the template   
It will look for the template file in the 'templates/' directory by default  

    render_template(
        "welcome.html",
        message="Here's a message from the View!"
    )

## Static files:
Directory name: 'static'  
Contains static files like
- css
- js
- images


### directory sturcture
```
static/
    flask.jpg
    my.js
    style.css
templates/
    welcome.html
mywelcomeapp.py
```

## _example code_:
```python
from flask import Flask, render_template
from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the View!"
    )
```
_example template_
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>JinJa2 Templates</title>
    </head>
    <body>
        <h1>Welcome to my JinJa2 Templates page!</h1>
        <h2> {{message}} </h2>
        <img src="/static/flasklogo.jpg">
    </body>
</html>
```
