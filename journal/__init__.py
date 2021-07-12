from flask import Flask, render_template
import sys
from pymongo import MongoClient

client = MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.scjiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.gettingStarted


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'
    from .views import main_views, register_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(register_views.bp)
    return app


