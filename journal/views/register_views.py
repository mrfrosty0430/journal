from flask import Blueprint,render_template
from pymongo import MongoClient

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/',methods=(['POST','GET']))
def new_post():
    client = MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.scjiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.gettingStarted
    people = db.people
    print(people.find_one())
    return render_template('register.html')

 