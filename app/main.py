from flask import Flask
from app.routes import register_route

app = Flask(__name__)

register_route(app)