from datetime import datetime

from app import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(150))
    data_create = db.Column(db.DateTime, default=datetime.now)
