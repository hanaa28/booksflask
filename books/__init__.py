from flask import Blueprint


book_blueprint = Blueprint("books",__name__,url_prefix="/books")

from app.books import views