from models.index import db, Post

def create_post(data):
    new_post = Post(data['title'], data['message'], data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return new_post.serialize()