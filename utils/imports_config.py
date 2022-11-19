#FLASK
from flask import Blueprint
from flask import Flask,session,render_template,url_for,redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

#FLASK-ADMIN
from flask_admin.contrib.sqla import ModelView  
from flask_admin.menu import MenuLink
from flask_admin import Admin
from utils.imports_admin import *
from flask_admin import AdminIndexView

#UTILS
from utils.db import db

#OTHERS
from unicodedata import category