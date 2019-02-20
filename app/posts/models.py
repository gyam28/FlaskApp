from app import db
from datetime import datetime



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60),nullable=False)
    subtitle = db. Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
