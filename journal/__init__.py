from flask import Flask, render_template
import sys


def create_app():
    app = Flask(__name__)
    from .views import main_views, register_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(register_views.bp)
    return app


