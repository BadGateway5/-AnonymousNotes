from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.blueprints.user import user
app.register_blueprint(user)