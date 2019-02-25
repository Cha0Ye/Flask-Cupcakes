from flask import Flask, jsonify, request, redirect, render_template
from models import db, connect_db, Cupcakes
from flask_debugtoolbar import DebugToolbarExtension

from flask_wtf import FlaskForm
#from forms import AddNewPetForm, EditPetForm
from flask_sqlalchemy import SQLAlchemy

DEFAULT_PHOTO = 'https://shenandoahcountyva.us/bos/wp-content/uploads/sites/4/2018/01/picture-not-available-clipart-12.jpg'

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
#db.create_all()


@app.route('/cupcakes', methods=["GET"])
def show_all_cupcakes():
    '''show all cupcakes'''
    cupcakes = Cupcakes.query.all()
    serialized_cupcakes = [{'flavor':cupcake.flavor, 'size':cupcake.size, 'rating':cupcake.rating, 'image':cupcake.image} for cupcake in cupcakes]
    return jsonify(response=serialized_cupcakes)