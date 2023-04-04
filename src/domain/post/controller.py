import domain.post.repository as Repository
import handel_response as Response
import domain.user.controller as UserController

def create_post(body):
    if body['title'] is None or body['title'] == '':
        return Response.response_error('title require', 400)
    
    user = UserController.get_user_by_id(body['user_id'])

    if user is None:
        return Response.response_error('user no valid', 400)
    
    return Repository.create_post(body)
    

