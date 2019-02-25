
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


def connect_db(app):
        """ connect to db"""
        db.app = app
        db.init_app(app)

Class Cupcakes(db.Model):
    ''' SQLALChemy Cupcakes class'''
    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key=True, 
                   autoincrement=True)

    flavor = db.Column(db.Text, 
                       nullable=False)
    size = db.Column(db.Text, 
                     nullable=False)

    rating = db.Column(db.Float, 
                       nullable=False)

    image = db.Column(db.Text, 
            default='https://tinyurl.com/truffle-cupcake')