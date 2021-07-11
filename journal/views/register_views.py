from flask import Blueprint,render_template

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/',methods=(['POST','GET']))
def new_post():
    return render_template('register.html')

