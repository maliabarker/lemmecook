from lemmecook_app.extensions import app
from lemmecook_app.main.routes import main

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(port=5003, host='0.0.0.0')