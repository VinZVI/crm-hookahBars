from flask_wtf import FlaskForm

from crmapp.menu.models import Category, Item

from wtforms import HiddenField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

class CategoryForm(FlaskForm):
    category_name = StringField(
        'Название категории',
        validators=[DataRequired(), Length(min=3, max=25)],
        render_kw={
            "class": "form-control",
            "placeholder": "Название Категории"
        }
    )

    category_description = StringField(
        'Описание категории',
        validators=[Length(min=5, max=60)],
        render_kw={
            "class": "form-control",
            "placeholder": "Описание Категории"
        }    
    )

    hookah_id = HiddenField(
        'ID кальянной',
        validators=[DataRequired()]
    )

    user_id = HiddenField(
        'ID пользователя',
        validators=[DataRequired()]
    )

    submit = SubmitField(
        'POST',
        render_kw={"class": "btn btn-primary"}
    )

    def validate_categoryname(self, category_name: StringField) -> Exception:
        category = Category.query.filter_by(category_name=category_name.data).first()
        if category.category_name == category_name:
            raise ValidationError('Такая категория уже существует.')

class CategoryDeleteForm(FlaskForm):
    category_name = StringField(
        'Название категории',
        validators=[Length(min=3, max=25)],
        render_kw={
            "class": "form-control",
            "placeholder": "Название Категории"
        }
    )

    hookah_id = HiddenField(
        'ID кальянной',
        validators=[DataRequired()]
    )

    submit = SubmitField(
        'DELETE',
        render_kw={"class": "btn btn-primary"}
    )

class ItemForm(FlaskForm):
    item_name = StringField(
        'Название позиции',
        validators=[DataRequired(), Length(max=50)],
        render_kw={
            "class": "form-control",
            "placeholder": "Название позиции"
        }
    )

    item_description = StringField(
        'Описание позиции',
        validators=[Length(max=150)],
        render_kw={
            "class": "form-control",
            "placeholder": "Описание позиции"
        }
    )

    price = IntegerField(
        'Цена',
        validators=[DataRequired(), NumberRange(max=50000)],
        render_kw={
            "class": "form-control",
            "placeholder": "Цена"
        }
    )

    availability = IntegerField(
        'Остаток',
        validators=[NumberRange(max=10000)],
        render_kw={
            "class": "form-control",
            "placeholder": "Остаток"
        }
    )

    category_id = HiddenField(
        'ID категории',
        validators=[DataRequired()]
    )

    hookah_id = HiddenField(
        'ID кальянной',
        validators=[DataRequired()]
    )

    user_id = HiddenField(
        'ID пользователя',
        validators=[DataRequired()]
    )

    submit = SubmitField(
        'POST',
        render_kw={"class": "btn btn-primary"}
    )

    def validate_itemname(self, item_name: StringField) -> Exception:
        item = Item.query.filter_by(item_name=item_name.data).first()
        if item.item_name == item_name:
            raise ValidationError('Такая позиция уже существует.')

class ItemDeleteForm(FlaskForm):
    item_name = StringField(
        'Название позиции',
        validators=[Length(max=50)],
        render_kw={
            "class": "form-control",
            "placeholder": "Название позиции"
        }
    )

    category_id = HiddenField(
        'ID категории',
        validators=[DataRequired()]
    )

    hookah_id = HiddenField(
        'ID кальянной',
        validators=[DataRequired()]
    )

    submit = SubmitField(
        'DELETE',
        render_kw={"class": "btn btn-primary"}
    )