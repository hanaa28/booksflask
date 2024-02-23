
from app.books import book_blueprint
from app.models import Book, db 
from flask_restful import Resource,Api, fields, marshal_with
from flask import request
from app.books.parsers import books_parser

@book_blueprint.route("/api" , endpoint="api")
def get_books():
    book = Book.query.all()
    bks = []
    for bk in book:
        bk_data = bk.__dict__
        del bk_data["_sa_instance_state"]
        bks.append(bk_data)
    print(bks)
    return bks


category_serilizer = {
     "id": fields.Integer,
    "name":fields.String,
    "description":fields.String,
}


book_serilizer = {
     "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "num_pages":fields.Integer,
    "price": fields.Integer,
    "Category_id": fields.Integer,
    "category_name": fields.Nested(category_serilizer)
}


class BookList(Resource):
    @marshal_with(book_serilizer)
    def get(self):
        books = Book.query.all()
        return books, 200
    
    
    @marshal_with(book_serilizer)
    def post(self):
        print(request.data)
        book_data = books_parser.parse_args()
        print(book_data)
        book = Book.save_book(book_data)
        return book , 201
    

class BookResource (Resource):
    @marshal_with(book_serilizer)
    def get(self, id):
        book =Book.get_book_by_id(id)
        return book, 200
    @marshal_with(book_serilizer)
    def put(self):
        book =Book.get_book_by_id(id)
        if book:
            book_data = books_parser.parse_args()
            book.name = book_data["name"]
            book.image = book_data["image"]
            book.price =book_data["price"]
            book.num_pages = book_data["num_pages"]
            book.Category_id =book_data["Category_id"]
            db.session.add(book)
            db.session.commit()
            return book

    def delete(self,id):
        book= Book.delete_book_by_id(id)
        return book,204
        
        
    


    