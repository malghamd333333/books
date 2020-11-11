from flask import Blueprint , render_template , request , jsonify
from app.models import Auth, Books
from app import db
from app.authentication import AuthError, requires_auth



main = Blueprint('main' , __name__)

@main.route("/")
def index():
    all_books = Books.query.all()
    return render_template("index.html" , data = all_books)


