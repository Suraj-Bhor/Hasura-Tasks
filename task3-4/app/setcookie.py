from app import app
from flask import render_template
from flask import request, Response

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookies():
    if(request.method == 'POST'):
        user = request.form.get('nm')
        age = request.form.get('age')
        resp = Response(render_template('readcookie.html'))
        resp.set_cookie('Name', user)
        resp.set_cookie('Age', age)
    return resp
