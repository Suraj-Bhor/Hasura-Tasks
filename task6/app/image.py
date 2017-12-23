from app import app
from flask import render_template
@app.route('/image')

def image():
     return render_template('page.html',title='Image')
