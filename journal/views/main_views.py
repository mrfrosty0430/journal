from flask import Blueprint,render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def main_page():
    return render_template('index.html')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/wtf')
def hello_d():
    return 'Hello, wtf!'
