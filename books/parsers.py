from flask_restful import reqparse

books_parser = reqparse.RequestParser()
books_parser.add_argument('name', type=str, required=True, help='Name of the book is required')
books_parser.add_argument('image', type=str)
books_parser.add_argument('num_pages', type=int)
books_parser.add_argument('price', type=float)
books_parser.add_argument('Category_id', type=int)