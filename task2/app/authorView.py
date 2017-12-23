from app import app
from flask import render_template
import json, urllib
@app.route('/author')

def author():
    #filename = 'users.json'
    url = "https://jsonplaceholder.typicode.com/users"
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    return render_template('author.html',title='Author',data=data)
