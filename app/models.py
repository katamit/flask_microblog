from datetime import datetime
from app import db, login

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Flask-Login keeps track of the logged in user by storing its unique identifier in Flask's user session,
# a storage space assigned to each user who connects to the application. Each time the logged-in user navigates to a
# new page, Flask-Login retrieves the ID of the user from the session, and then loads that user into memory.

# Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. For that
# reason, the extension expects that the application will configure a user loader function, that can be called to
# load a user given the ID.
@login.user_loader
def load_user(idx):
    return User.query.get(int(idx))


class User(UserMixin, db.Model):
    # __tablename__ = 'USER'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # This is not an actual database field, but a high - level view of the relationship between users and posts,
    # and for that reason it isn't in the database diagram. For a one-to-many relationship, a db.relationship field
    # is normally defined on the "one" side, and is used as a convenient way to get access to the "many".

    # the relationship that I created in the this (User) class adds a posts attribute to users, and also a author
    # attribute to posts.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


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
