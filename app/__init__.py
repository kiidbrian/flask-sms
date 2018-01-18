from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import config
import os

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

app = Flask(__name__)

CORS(app)
env = os.environ.get('FLASK_ENV', 'dev')
app.config.from_object(config[env])

db = SQLAlchemy(app)
db.create_all()
db.session.commit()

login_manager.init_app(app)

# import and register blueprints
from app.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
