import domain.user.repository as Repository
import handel_response as Response

def create_user(data):
    if data['email'] is None or data['email'] == '':
        return Response.response_error( 'Email not valid', 400)
    
    if data['username'] is None or data['username'] == '':
        return Response.response_error( 'user not valid', 400)
    
    return Repository.create_user(data), 201

def get_user_by_id(user_id):
    user = Repository.get_user_by_id(user_id)

    if user is None:
        return Response.response_error( 'user not found', 404)
    
    return user

def get_all_users():
    all_users = Repository.get_all_users()
    return Response.response_ok(all_users)