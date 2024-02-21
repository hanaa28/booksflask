from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)
    num_pages = db.Column(db.Integer)  
    price = db.Column(db.Float)       
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
    
    @property
    def image_url(self):
        return url_for('static',filename=f'books/images/{self.image}')
    
    @classmethod
    def get_book_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    @property
    def show_url(self):
        return url_for("books.books_show",id=self.id)
    
    @classmethod
    def delete_book_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    @property
    def delete_url(self):
        return url_for("books.book_delete",id=self.id)
    
    @property
    def edit_url(self):
        return url_for("books.book_edit",id=self.id)