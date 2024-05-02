from app import db
from datetime import datetime

bcrypt = Bcrypt()
from flask_bcrypt import Bcrypt


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    origin = db.Column(db.String(200))

    
    
    
    
    
    
    
    
    
    # Change the relationship to 'books' (lowercase) since it's referencing the 'Book' model
    # books = db.relationship('Book', backref='author', lazy=True)

    # def __init__(self, first_name, last_name, email, contact, password, user_type='author', biography=None):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.contact = contact
    #     self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    #     self.user_type = user_type
    #     self.biography = biography

    # def get_full_name(self):
    #     return f"{self.last_name} {self.first_name}"

    # def check_password(self, password):
    #     return bcrypt.check_password_hash(self.password, password)
