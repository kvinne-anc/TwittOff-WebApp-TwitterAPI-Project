# web_app/__init__.py

from flask import Flask, escape, request
from flask import Blueprint

#home_routes = Blueprint("home_routes", __name__)


from web_app.routes.home_routes import home_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)