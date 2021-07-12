from flask import Blueprint,render_template
from pymongo import MongoClient

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/',methods=(['POST','GET']))
def new_post():
    client = MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.scjiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.gettingStarted
    journal = db.journal
    
    journal.insert_one({
        "sleep":"00",
        "wake":"06.5",
        "emotions":["happy","sad","miserable","lonely","depressed"],
        "thoughts":"just a lonely day,didn't do much"
        
    })

    return render_template('register.html')

 