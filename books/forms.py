
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Category

class BookForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired()] )
    image= StringField("Image")
    num_pages= IntegerField("Number of pages")
    price= IntegerField("Price", validators=[DataRequired()])
    Category_id = QuerySelectField("Category", query_factory=lambda:Category.get_all_category())



