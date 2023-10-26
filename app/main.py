from flask import Flask
from flask_cors import CORS
from app.routes import register_route

app = Flask(__name__)
CORS(app)

register_route(app)