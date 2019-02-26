from flask import Flask, jsonify, request, redirect, render_template
from models import db, connect_db, Cupcakes
from flask_debugtoolbar import DebugToolbarExtension

# from flask_wtf import FlaskForm
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

@app.route('/')
def render_index_page():
    '''renders index page'''
    return render_template('index.html')

@app.route('/cupcakes', methods=["GET"])
def show_all_cupcakes():
    '''return JSON list of all cupcakes in dictionaries

    [{'flavor':..., 'size': ...,
    'rating':..., 'image':image}, {...}]

    '''
    cupcakes = Cupcakes.query.all()
    serialized_cupcakes = [{'flavor': cupcake.flavor,
                            'size': cupcake.size,
                            'rating': cupcake.rating,
                            'image': cupcake.image} for cupcake in cupcakes]
    return jsonify(response=serialized_cupcakes)


@app.route('/cupcakes', methods=["POST"])
def add_cupcake():
    '''Take in JSON data and add cupcake to database
       Return dictionary of new cupcake.

    "{'id': ..., 'flavor': ..., 'size': ...,
    'rating': ..., 'image': ...}"

    '''

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image'] or None

    new_cupcake = Cupcakes(flavor=flavor,
                           size=size,
                           rating=rating,
                           image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    new_cupcake_dict = {'id': new_cupcake.id, 'flavor': flavor,
                        'size': size, 'rating': rating, 'image': image}
    return jsonify(response=new_cupcake_dict)


@app.route('/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    ''' update a current cupcake by its id modifying all fields

    "{'id': ..., 'flavor': ..., 'size': ...,
    'rating': ..., 'image': ...}"

    '''
    cupcake_to_modify = Cupcakes.query.get(id)
    cupcake_to_modify.flavor = request.json['flavor']
    cupcake_to_modify.size = request.json['size']
    cupcake_to_modify.rating = request.json['rating']
    cupcake_to_modify.image = request.json['image']

    db.session.commit()

    updated_cupcake_dict = {'id': id,
                            'flavor': cupcake_to_modify.flavor,
                            'size': cupcake_to_modify.size,
                            'rating': cupcake_to_modify.rating,
                            'image': cupcake_to_modify.image}
    return jsonify(response=updated_cupcake_dict)


@app.route('/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    ''' update a current cupcake by its id modifying all fields'''
    cupcake_to_delete = Cupcakes.query.get(id)
    db.session.delete(cupcake_to_delete)
    db.session.commit()

    return jsonify(response={"message": "Deleted"})
