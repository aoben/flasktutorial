
from flaskblog import db
from datetime import datetime


class User(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(20), unique = True)
        email = db.Column(db.String(80), nullable = False)
        password = db.Column(db.String(80), nullable = False)
        image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
        posts = db.relationship('Post', backref = 'author', lazy = True)

        def __repr__(self):
                return "%s, %s, %s" %( self.image_file, self.username, self.email)
        
class Post(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        title = db.Column(db.String, nullable = False)
        content = db.Column(db.Text, nullable = False)
        date_posted = db.Column(db.DateTime, default = datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
