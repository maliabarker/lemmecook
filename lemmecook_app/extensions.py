from flask import Flask
from pymongo import MongoClient
import os
from lemmecook_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY')

# ======= DB Setup ==========
uri = os.environ.get('MONGODB_URI')
client = MongoClient(uri)
my_db = os.environ.get('MONGODB_DATABASE')
db = client.get_database(my_db)

# ======= Collections ==========
recipes = db.recipes
ingredients = db.ingredients
tools = db.tools

with app.app_context():
    from lemmecook_app.main.forms import RecipeForm
    recipe_form = RecipeForm
