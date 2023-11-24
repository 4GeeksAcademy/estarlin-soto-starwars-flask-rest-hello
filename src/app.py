"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets



app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people')
def get_all_people():
    
    all_people = People.query.all()
    people_list = [{
        "id":  people.id, 
        'name': people.name, 
        'eye_color' : people.eye_color, 
        'skin_color' : people.skin_color,
        'height' : people.height,
        'hair_color' : people.hair_color,
        'birth_year' : people.birth_year, 
        'gender' : people.gender,   
        'mass' : people.mass    
        } 
        for people in all_people]       
        
    return jsonify(people_list), 200
    
    
@app.route('/people/<int:char_id>')
def get_people_by_id(char_id):
    people = People.query.get(char_id)
    if people:
        return jsonify({
             "id":  people.id, 
            'name': people.name, 
            'eye_color' : people.eye_color, 
            'skin_color' : people.skin_color,
            'height' : people.height,
            'hair_color' : people.hair_color,
            'birth_year' : people.birth_year, 
            'gender' : people.gender,
            'mass' : people.mass,       
            }), 200
    else :
        return {'msg' : 'That user dont exist :('}

@app.route('/people/create', methods=['POST'])
def create_new_char():

    new_people = People(
        name = request.json.get('name'), 
        eye_color =  request.json.get('eye_color'), 
        skin_color =  request.json.get('skin_color'),
        height = request.json.get('height'),
        mass = request.json.get('mass'),
        hair_color = request.json.get('hair_color'),
        birth_year = request.json.get('birth_year'),
        gender = request.json.get('gender'),
        )
    db.session.add(new_people)
    db.session.commit()
    return jsonify({
            'id': new_people.id,
            'name' : new_people.name,
            'eye_color': new_people.eye_color,
            'skin_color' : new_people.skin_color,
            'mass' : new_people.mass,
            'hair_color' : new_people.hair_color,
            'height' : new_people.height,
            'birth_year' : new_people.birth_year,
            'gender' : new_people.gender
            }), 200

@app.route('/people/edit/<int:char_id>', methods=['PUT'])
def edit_char_by_id(char_id):

    char_from_db = People.query.get(char_id)

    if char_from_db:   
        char_from_db.name = request.json.get('name')
        char_from_db.eye_color =  request.json.get('eye_color')
        char_from_db.skin_color =  request.json.get('skin_color')
        char_from_db.mass = request.json.get('mass')
        char_from_db.hair_color = request.json.get('hair_color')
        char_from_db.height = request.json.get('height')
        char_from_db.birth_year = request.json.get('birth_year')
        char_from_db.gender = request.json.get('gender')
        db.session.commit()

        return jsonify({
            'id' : char_from_db.id,
            'name' : char_from_db.name,
            'eye_color' : char_from_db.eye_color,
            'skin_color' : char_from_db.skin_color,
            'hair_color' : char_from_db.hair_color,
            'height' : char_from_db.height,
            'birth_year' : char_from_db.birth_year,
            'gender' : char_from_db.gender,
            'mass' : char_from_db.mass,
            
        }), 200
    else:
        return jsonify({
            'msg' : 'that char dont exits'
        }), 404
    
@app.route('/people/delete/<int:char_id>', methods=['DELETE'])
def delete_char_by_id(char_id):
    user_exist_db = People.query.get(char_id)

    if user_exist_db:
        db.session.delete(user_exist_db)
        db.session.commit()
        return jsonify({
            'msg' : 'character deleted!!'
        })
    else:
        return jsonify({
            'msg' : 'this character not exist :(' 
        })

#planets end points

@app.route('/planets')
def get_all_planets():
    
    all_planets = Planets.query.all()
    planets_list = [{
        "id": planet.id, 
        'planet_name': planet.planet_name, 
        'rotation_period' : planet.rotation_period, 
        'orbital_period' : planet.orbital_period,
        'diameter' : planet.diameter,
        'climate' : planet.climate,
        'gravity' : planet.gravity, 
        'terrain' : planet.terrain,   
        'surface_water' : planet.surface_water,
        'population' : planet.population       
        } 
        for planet in all_planets]       
        
    return jsonify(planets_list), 200

    
@app.route('/planets/<int:planet_id>')
def get_planet_by_id(planet_id):
    planet = Planets.query.get(planet_id)
    if planet:
        return jsonify({
             "id":  planet.id, 
            'planet_name': planet.planet_name, 
            'rotation_period' : planet.rotation_period, 
            'orbital_period' : planet.orbital_period,
            'diameter' : planet.diameter,
            'climate' : planet.climate,
            'gravity' : planet.gravity, 
            'surface_water' : planet.surface_water,
            'terrain' : planet.terrain,   
            'population' : planet.population,      
            }), 200
    else :
        return {'msg' : 'That planet not exist :('}

@app.route('/planets/create', methods=['POST'])
def create_new_planet():

    new_planet = Planets(
        planet_name = request.json.get('planet_name'), 
        rotation_period =  request.json.get('rotation_period'), 
        orbital_period =  request.json.get('orbital_period'),
        diameter = request.json.get('diameter'),
        climate = request.json.get('climate'),
        gravity = request.json.get('gravity'),
        surface_water = request.json.get('surface_water'),
        terrain = request.json.get('terrain'),
        population = request.json.get('population'),
        )
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({
            "id":  new_planet.id, 
            'planet_name': new_planet.planet_name, 
            'rotation_period' : new_planet.rotation_period, 
            'orbital_period' : new_planet.orbital_period,
            'diameter' : new_planet.diameter,
            'climate' : new_planet.climate,
            'gravity' : new_planet.gravity, 
            'surface_water' : new_planet.surface_water,
            'terrain' : new_planet.terrain,   
            'population' : new_planet.population,     
            }), 200

@app.route('/planets/edit/<int:planet_id>', methods=['PUT'])
def edit_planet_by_id(planet_id):

    planet_from_db = Planets.query.get(planet_id)

    if planet_from_db:   
        planet_from_db.planet_name = request.json.get('planet_name')
        planet_from_db.rotation_period = request.json.get('rotation_period')
        planet_from_db.orbital_period = request.json.get('orbital_period')
        planet_from_db.diameter = request.json.get('diameter')
        planet_from_db.climate = request.json.get('climate')
        planet_from_db.gravity = request.json.get('gravity')
        planet_from_db.surface_water = request.json.get('surface_water')
        planet_from_db.terrain = request.json.get('terrain')
        planet_from_db.population = request.json.get('population')
        db.session.commit()

        return jsonify({
            'id' : planet_from_db.id,
            'planet_name' : planet_from_db.planet_name,
            'rotation_period' : planet_from_db.rotation_period,
            'orbital_period' : planet_from_db.orbital_period,
            'diameter' : planet_from_db.diameter,
            'climate' : planet_from_db.climate,
            'gravity' : planet_from_db.gravity,
            'surface_water' : planet_from_db.surface_water,
            'terrain' : planet_from_db.terrain,
            'population' : planet_from_db.population,    
            
        }), 200
    else:
        return jsonify({ 'msg' : 'that Planet not exits' }), 404
    
@app.route('/planets/delete/<int:planet_id>', methods=['DELETE'])
def delete_planet_by_id(planet_id):
    planet_exist_db = Planets.query.get(planet_id)

    if planet_exist_db:
        db.session.delete(planet_exist_db)
        db.session.commit()
        return jsonify({
            'msg' : 'planet deleted!!'
        })
    else:
        return jsonify({
            'msg' : 'this planet not exist :(' 
        })

# User End points
@app.route('/users')
def get_all_users():
    all_users = User.query.all()
    list_of_users = [{
        'user_name' : user.user_name,

    } for user in all_users]
    return jsonify(list_of_users), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3020))
    app.run(host='0.0.0.0', port=PORT, debug=False)
