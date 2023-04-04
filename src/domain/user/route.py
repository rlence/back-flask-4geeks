from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller

#SOLID - OBJ - FUNC - S -> SINGLE RESPONSABILITY 

def user_route(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        return Controller.create_user(body)
    
    @app.route('/user', methods=['GET'])
    def get_all_users():
        return Controller.get_all_users()

    @app.route('/user/<int:id>', methods=['GET'])
    def get_user(id):
        return Controller.get_user_by_id(id)

