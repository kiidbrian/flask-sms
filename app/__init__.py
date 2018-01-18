from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import config
import os

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy(app)

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  CORS(app)

  login_manager.init_app(app)
  db.init_app(app)

  # import and register blueprints
  from app.auth import auth as auth_blueprint

  app.register_blueprint(auth_blueprint)

  return app
