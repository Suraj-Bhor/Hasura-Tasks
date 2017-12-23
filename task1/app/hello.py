from app import app
from flask import render_template
@app.route('/')
def index():
    user = {'name':'Suraj'}
    return render_template('index.html',title='Home',user=user)
