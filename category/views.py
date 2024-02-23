from app.category import category_blueprint
from app.models import Category
from flask import render_template
from flask import render_template,redirect
from flask import url_for
from app.models import db
from app.category.forms import CategoryForm



@category_blueprint.route('/home', methods=['GET'] , endpoint='home')
def home():
    return "<h1> Welcome Home </h1>"


@category_blueprint.route('/', methods=['GET'] , endpoint='index')
def category_index():
    categories = Category.get_all_category()
    return render_template("categories/index.html", categories=categories)

@category_blueprint.route('/create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories.index'))
    return render_template('categories/create_category.html', form=form)


@category_blueprint.route("/delete/<int:id>", endpoint="category_delete")
def delete_category(id):
    category_to_delete = Category.delete_category_by_id(id)
    db.session.delete(category_to_delete)
    db.session.commit()
    return redirect(url_for('categories.index'))

@category_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'] , endpoint="category_edit")
def edit_category(id):
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        db.session.commit()
        return redirect(url_for('categories.index'))
    return render_template('categories/edit.html', form=form, category=category)
