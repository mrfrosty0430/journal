from flask import Blueprint,render_template

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/')
def search_page():
    return render_template("search.html")


