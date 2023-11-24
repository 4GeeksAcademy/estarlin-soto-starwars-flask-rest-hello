from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)  

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    height = db.Column(db.String(20), unique=False, nullable=False)
    mass = db.Column(db.String(50), unique=False, nullable=False)
    eye_color = db.Column(db.String(50), unique=False, nullable=False)
    skin_color = db.Column(db.String(50), unique=False, nullable=False)
    hair_color = db.Column(db.String(50), unique=False, nullable=False)
    birth_year = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=False)

class Planets (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(50), unique=True, nullable=False)
    rotation_period = db.Column(db.String(20), unique=False, nullable=False)
    orbital_period = db.Column(db.String(20), unique=False, nullable=False)
    diameter = db.Column(db.String(20), unique=False, nullable=False)
    climate = db.Column(db.String(20), unique=False, nullable=False)
    gravity = db.Column(db.String(20), unique=False, nullable=False)
    terrain = db.Column(db.String(20), unique=False, nullable=False)
    surface_water = db.Column(db.String(20), unique=False, nullable=False)
    population = db.Column(db.String(20), unique=False, nullable=False)

class Favorites (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_fav = db.Column(db.String(50), unique=True, nullable=False)
    char_fav = db.Column(db.String(50), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.id
    
    def __repr__(self):
        return '<People %r>' % self.id 
    
    def __repr__(self):
        return '<Planets %r>' % self.id 
    
    def __repr__(self):
        return '<Favorites %r>' %self.id

    def serialize(self):
        return {
            #serializacion de la tabla users
            "id": self.id,
            "user_name" : self.user_name,
            "email": self.email, 
     
            #serializacion de la tabla people 
            "people_id" : self.people_id,
            "people_name": self.people_name,
            "eye_color": self.eye_color,
            "skin_color" : self.skin_color,
            "height" :  self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,

      
            #serializacion de la tabla planets
            "id" : self.id,
            "planet_name" : self.planet_name,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "diameter" : self.diameter,
            "climate" : self.climate,
            "gravity" : self.gravity,
            "terrain"  : self.terrain,
            "surface_water" : self.surface_water,
            "population" : self.population,
            
            #
             "id" : self.id,
            "planet_fav" : self.planet_fav,
            "people_fav" : self.people_fav,
            
        }