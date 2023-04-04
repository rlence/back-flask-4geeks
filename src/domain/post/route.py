from flask import request, jsonify
import domain.post.controller as Controller

def post_router(app):

    @app.route('/post', methods=['POST'])
    def create_post():
        body = request.get_json()
        new_post = Controller.create_post(body)
        return jsonify(new_post), 201