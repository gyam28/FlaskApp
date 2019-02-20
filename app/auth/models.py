from app import db, login_manager
from app.posts.models import Post
from wtforms.validators import ValidationError
from flask_login import UserMixin #class that contains the 4 methods required by flask_login
        # mts.are is_authenticated,is-active, is anonymous,get_id

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file=db.Column(db.String(20),nullable=False, default="default.jpg")
    password=db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post',backref='author', lazy=True) #lazy=the way to query a database

    def __repr__(self):
        return f"User('{self.username}, {self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
