from app import app
from flask import render_template
from flask import request, Response

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('Name')
   age = request.cookies.get('Age')
   return '<h1>Welcome '+name+'</h1><h2>Your age is '+age+'</h2>'