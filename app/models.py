from datetime import datetime
from app import db


class User(db.Model):
    # __tablename__ = 'USER'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # This is not an actual database field, but a high - level view of the relationship between users and posts,
    # and for that reason it isn't in the database diagram. For a one-to-many relationship, a db.relationship field
    # is normally defined on the "one" side, and is used as a convenient way to get access to the "many".
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


# It is an unfortunate inconsistency that in some instances such as in a db.relationship() call, the model is
# referenced by the model class, which typically starts with an uppercase character, while in other cases such as
# this db.ForeignKey() declaration, a model is given by its database table name, for which SQLAlchemy automatically
# uses lowercase characters and, for multi-word model names, snake case.


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
