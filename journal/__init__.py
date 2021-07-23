from flask import Flask, render_template
import sys
from pymongo import MongoClient
from decouple import config

db_url = config('DB')
client = MongoClient(db_url)
db = client.gettingStarted



def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'
    from .views import main_views, register_views, load_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(register_views.bp)
    app.register_blueprint(load_views.bp)
    return app


