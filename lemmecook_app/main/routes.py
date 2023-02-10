from flask import Blueprint, request, render_template, redirect, url_for, flash
from bson.objectid import ObjectId
from lemmecook_app.main.forms import ToolForm
from lemmecook_app.extensions import db, recipe_form
main = Blueprint("main", __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    recipes = db.recipes.find()
    return render_template('index.html', recipes=recipes)


@main.route('/index-recipes', methods=['GET'])
def view_all_recipes():
    recipes = db.recipes.find()
    return render_template('index_recipes.html', recipes=recipes)


@main.route('/new-tool', methods=['GET', 'POST'])
def new_tool():
    form = ToolForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Tool form validated')
            photo = request.files["photo"]
            if not photo.filename.endswith(".png"):
                flash("Only PNG files are allowed", 'danger')
                redirect(url_for('main.new_tool'))
            photo_data = photo.read()
            # Create new tool
            db.tools.insert_one(
                {
                    'name': form.tool_name.data,
                    'location': form.location.data,
                    'photo': photo_data
                }
            )
            flash('Tool uploaded successfully!', 'success')
            return redirect(url_for('main.home'))
    return render_template('new_tool.html', form=form)


@main.route('/new-recipe', methods=['GET', 'POST'])
def new_recipe():
    form = recipe_form()
    for ing_form in form.ingredients:
        ing_form.tool.choices = [(item['_id'], item['name']) for item in db.tools.find()]
        print(ing_form.tool.choices)
        
    if request.method == 'POST':
        if form.add_ingredient.data:
            getattr(form, 'ingredients').append_entry()
            for ing_form in form.ingredients:
                ing_form.tool.choices = [(item['_id'], item['name']) for item in db.tools.find()]
                print(ing_form.tool.choices)
            return render_template('new_recipe.html', form=form)
        if form.validate_on_submit():
            print('Recipe form validated')
            recipe_photo = request.files["photo"]
            if not recipe_photo.filename.endswith(".png"):
                flash("Only PNG files are allowed", 'danger')
                redirect(url_for('main.new_tool'))
            recipe_photo_data = recipe_photo.read()
            ingredient_list = []
            for field in form.ingredients:
                ingredient = {
                    'name': field.ingredient_name.data,
                    'measurement': field.measurement.data,
                    'tool': db.tools.find_one({'_id': ObjectId(field.tool.data)}),
                    'location': field.location.data,
                    'photo': field.photo.data.read(),
                    'notes': field.notes.data
                }
                ingredient_list.append(ingredient)
            # Create new recipe
            db.recipes.insert_one(
                {
                    'name': form.recipe_name.data,
                    'description': form.description.data,
                    'cuisine_type': form.cuisine_type.data,
                    'ingredients': ingredient_list,
                    'cook_time': form.cook_time.data,
                    'instructions': form.instructions.data,
                    'has_cooked': form.has_cooked.data,
                    'photo': recipe_photo_data
                }
            )
            flash('Recipe uploaded successfully!', 'success')
            return redirect(url_for('main.home'))
    return render_template('new_recipe.html', form=form)


@main.route('/edit-recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = db.recipes.find_one({'_id', recipe_id})
    form = recipe_form(recipe)
    if request.method == 'POST':
        if form.validate_on_submit():
            # update recipe
            pass
    return render_template('edit_recipe.html', form=form)
