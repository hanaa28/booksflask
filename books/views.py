from flask import render_template,redirect
from app.models import Book
from app.books import book_blueprint
from flask import request
from datetime import datetime
from flask import url_for
from app.models import db
from werkzeug.utils import secure_filename
import os




UPLOAD_FOLDER = 'static/books/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@book_blueprint.route('', endpoint='books_index')
def books_index():
    books = Book.get_all_objects()
    return render_template("book/book.html", books=books)


@book_blueprint.route("/<int:id>", endpoint="books_show")
def books_show(id):
    book= Book.get_book_by_id(id)
    return render_template("book/show.html", book=book)

@book_blueprint.route("/create", methods=['GET', 'POST'], endpoint="book_create")
def book_create():
    if request.method == 'POST':
        image = request.files['image']
        image.save("{{book.image_url}}" + image.filename)  

        book = Book(
            name=request.form['name'],
            image=image.filename,
            num_pages=request.form['num_pages'],  
            price=request.form['price'],  
            created_at=datetime.utcnow()
        )

        db.session.add(book)
        db.session.commit()

        return redirect(book.show_url)

    return render_template("book/create.html")


@book_blueprint.route("/delete/<int:id>", endpoint="book_delete")
def delete_book(id):
    book_to_delete = Book.delete_book_by_id(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('books.books_index'))



@book_blueprint.route("/edit/<int:id>", methods=['GET', 'POST'], endpoint="book_edit")
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.name = request.form['name']
        book.price = request.form['price']
        book.num_pages = request.form['num_pages']
    
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                filename = secure_filename(image.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(image_path)
                book.image = filename

        book.updated_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('books.books_show', id=book.id))
    return render_template("book/edit.html", book=book)