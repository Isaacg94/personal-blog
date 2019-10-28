from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Comment:

    all_comments = []

    def __init__(self,post_id,title,comment):
        self.post_id = post_id
        self.title = title
        self.comment = comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comment(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.post_id == id:
                response.append(comment)

        return response




class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author,id,quote,permalink):
        self.author =author
        self.id = id
        self.quote = quote
        self.permalink = permalink


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'