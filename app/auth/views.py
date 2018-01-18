from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from . import auth
from datetime import datetime
from app import db


@auth.route('/', methods=['GET'])
def login():
    return render_template('index.html')
