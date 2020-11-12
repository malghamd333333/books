from flask import Blueprint , render_template , request , jsonify , session
from app.models import Auth, Books
from app import db
from app.authentication import AuthError, requires_auth



main = Blueprint('main' , __name__)

@main.route("/")
def index():
    login = False
    if "name"  in session:
        login = True
    all_books = Books.query.all()
    return render_template("index.html" , data = all_books , is_login=login)


