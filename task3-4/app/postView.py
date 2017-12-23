from app import app
from flask import render_template
import json, urllib
@app.route('/author')

def author():
    #filename = 'users.json'
    urlAuth = "https://jsonplaceholder.typicode.com/users"
    urlPosts = "https://jsonplaceholder.typicode.com/posts"
    responseAuth = urllib.urlopen(urlAuth)
    responsePosts = urllib.urlopen(urlPosts)
    dataAuth = json.loads(responseAuth.read())
    dataPosts = json.loads(responsePosts.read())

    return render_template('author.html',title='Author',dataAuth=dataAuth,dataPosts=dataPosts)
