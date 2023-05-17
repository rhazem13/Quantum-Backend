from models.db import db

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    photopath = db.Column(db.String(255))
    description = db.Column(db.Text)
    websiteurl = db.Column(db.String(255))