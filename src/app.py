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
from models import db, User
#from models import Person

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
    all_user = User.query.all()
    serialize_all_user = list(map(lambda user: user.to_json(), all_user))
    print(all_user)

    return jsonify(serialize_all_user), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    print(id)
    user = User.query.get(id)
    print(user)
    return jsonify(user.to_json()), 200

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data['email'], data['password'], data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify("HOLA SOY EL post DE LA RUTA user"), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int( 3001)
    app.run(host='0.0.0.0', port=3001, debug=False)
