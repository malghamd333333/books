from flask import Blueprint , render_template , request , jsonify
from app.models import Auth, Books
from app import db
from app.authentication import AuthError, requires_auth



main = Blueprint('main' , __name__)

@main.route("/")
@requires_auth()
def index(payload):
    print("----------------")
    print(payload)
    print("----------------")
    all_books = Books.query.all()
    return render_template("index.html" , data = all_books)


