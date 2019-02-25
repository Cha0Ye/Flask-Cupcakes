
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


def connect_db(app):
        """ connect to db"""
        db.app = app
        db.init_app(app)