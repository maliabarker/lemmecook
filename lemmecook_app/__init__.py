# initializing main and database
from flask import Flask
import os
from lemmecook_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

from lemmecook_app.main.routes import main
app.register_blueprint(main)

# from lemmecook_app.main.forms import RecipeForm
# with app.app_context():
#     recipe_form = RecipeForm()