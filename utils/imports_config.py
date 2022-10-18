#FLASK
from flask import Blueprint
from flask import Flask,session,render_template,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

#FLASK-ADMIN
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_admin import Admin
from utils.imports_admin import *

#UTILS
from utils.db import db

#OTHERS
from unicodedata import category