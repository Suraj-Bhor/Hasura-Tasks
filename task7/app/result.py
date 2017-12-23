from app import app
from flask import render_template
from flask import request, Response

@app.route('/result', methods=['POST', 'GET'])
def doPrint():
    if(request.method == 'POST'):
        user = request.form.get('nm')
        age = request.form.get('age')
        resp = Response(render_template('result.html'))
        print user
        print age
    return resp
