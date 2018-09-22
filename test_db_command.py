# coding: utf-8
from app import db
from app.models import  User, Post
u = User(username='john', email= 'ramesh@nomail.com',)
u = User(username='john', email= 'ramesh@nomail.com')
db.session.add(u)
db.session.commit()
u = User(username='sakshi', email= 'sakshi@nomail.com')
db.session.ad
db.session.add(u)
db.session.commit()
users = User.query.all()
users
for u in users:
    print(u.id, u.username)
    
User.query.count()
u = User.query.get(1)
u
p =Post(boyd='my first post!', author=u)
p =Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()
Post.query.all()
u = User.query.get(1)
u
posts = u.posts.all()
posts
u = User.query.get(2)
u.posts()
u.posts.all()
Post.query.all()
posts = Post.query.all()
for p in posts:
    print(p.user_id)
    
for p in posts:
    print(p.author)    
    
for p in posts:
    print(p.author.username)    
    
User.query
User.query.order_by(User.username.des()).all()
User.query.order_by(User.username.desc()).all()
User.query.all().order_by(User.username.desc())
users = User.query.all()
for u in users:
    db.session.delete(u)
    
for p in Post.query.all(): db.session.delete(p)
db.session.commit()
User.query.all()
