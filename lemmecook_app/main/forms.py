from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, BooleanField, FileField, FieldList, FormField, SubmitField, Form
from wtforms.validators import DataRequired, NumberRange, Optional


class IngredientForm(Form):
    ingredient_name = StringField('Ingredient Name')
    measurement = StringField('Measurements')
    tool = SelectField('Tool', choices=[])
    location = StringField('Location')
    photo = FileField('Photo')
    notes = TextAreaField('Ingredient Notes')


class ToolForm(FlaskForm):
    tool_name = StringField('Tool Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    notes = TextAreaField('Tool Notes', validators=[Optional()])
    submit = SubmitField('Submit Tool')


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    cuisine_type = StringField('Cuisine Type', validators=[Optional()])
    ingredients = FieldList(FormField(IngredientForm), 'Ingredients', validators=[DataRequired()], min_entries=1)
    add_ingredient = SubmitField('+ Ingredient')
    cook_time = FloatField('Cook Time', validators=[Optional()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    has_cooked = BooleanField('Have You Cooked This?', validators=[Optional()])
    photo = FileField('Add a Photo', validators=[Optional()])
    rating = FloatField('Star Rating (0-5)', validators=[Optional(), NumberRange(min=0, max=5)])
    submit = SubmitField('Submit Recipe')
