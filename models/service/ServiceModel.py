from models.db import db

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    photopath = db.Column(db.String(255))
    description = db.Column(db.Text)
    type = db.Column(db.Boolean)
