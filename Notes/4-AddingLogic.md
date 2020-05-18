# Adding Logic

- Pass value for a variable in the URL
- `url_for('func_name', var, varN)`
- `abort(404)`
- Jinja `if` conditionals
- Jinja `for` loops and loop.index0
- REST API

## Pass value for a variable in the URL
```
@app.route("/card/<int:x>")
def card_view(x=0):
```
Pass in a string
```
@app.route("/card/<x>")
```

## url_for('func_name', var, varN)
Instead of using the literal URL
```
<a href="/card">View Cards</a>
```
Use 'url_for()'
```
<a href="{{ url_for('card_view') }}">View Cards</a>
<a href="{{ url_for('card_view', index=3) }}">View Card</a>
<a href="{{ url_for('card_view', index=index+1) }}">View Card</a>
```

## abort(404)
```
from flask import Flask, abort
try:
    ...
except IndexError:
    abort(404)
```

## Jinja `if` conditionals
{% if index <= 0 %}  
{% else %}  
{% endif %}  

```
{% if index <= 0 %}
<a href="{{ url_for('card_view', index=max_index) }}">
    <button>GoTo End</button>
</a>
{% else %}
<a href="{{ url_for('card_view', index=index - 1) }}">
    <button>Prev Card</button>
</a>
{% endif %}
```

## Jinja `for` loops and loop.index0
{% for card in cards %}  
{% endfor %}

```
<ol>
    {% for card in cards %}
    <li>
        <a href="{{url_for('card_view', index=loop.index0)}}">{{card.question}}</a>
    </li>
    {% endfor %}
</ol>
```


## Serve data as a REST API
- URL path starts with '/api/'  
- returns json data  
- import jsonify

```
from flask import Flask, abort, jsonify
@app.route("/api/card")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
```

