from flask import Flask

app = Flask(__name__)
from app import views
from app import postView
from app import setcookie
from app import getcookie