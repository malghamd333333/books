from flask import Blueprint , render_template , request , flash , url_for
from app.models import Auth, Books
from app import db
from .forms import AddBook, AddAuth
from app.authentication import AuthError, requires_auth

 
admin = Blueprint('admin' , __name__  , url_prefix='/admin')
 
@admin.route("/")
def index():
    return "render_template(admin)"

     
@admin.route("/add_book" , methods=['POST' , 'GET'])
def add_book():
    form = AddBook(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        des = form.des.data
        page = form.page.data
        pub_year = form.pub_year.data
        auth_id = form.Auth_id.data

        new_book = Books(title=title, des=des , page=page , pub_year = pub_year , Auth_id = auth_id)
 
        db.session.add(new_book)
        db.session.commit()
        flash('New book added successfly', 'success')

        form.title.data  = ""
        form.des.data = ""
        form.page.data = ""
        form.pub_year.data = ""
        form.Auth_id.data = ""


    return render_template('add_book.html' , form=form , title='Add Book')


@admin.route("/<int:book_id>/update", methods=['GET', 'POST'])
def update_book(book_id):
    book = Books.query.get_or_404(book_id)
    form = AddBook(request.form)


    if request.method == 'POST' and form.validate():
        title = form.title.data
        des = form.des.data
        page = form.page.data
        pub_year = form.pub_year.data
        auth_id = form.Auth_id.data

        book.title = title
        book.des = des
        book.page = page
        book.pub_year = pub_year
        book.Auth_id = auth_id
        db.session.commit()

        flash('Book updeded successfly', 'success')

    form.title.data  = book.title
    form.des.data = book.des
    form.page.data = book.page
    form.pub_year.data = book.pub_year
    form.Auth_id.data = book.Auth_id

    return  render_template('add_book.html' , form=form ,  title='Update Book')
   
@admin.route("/<int:book_id>/delete", methods=['POST' , "GET"])
def delete_post(book_id):
    book = Books.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Your book has been deleted!', 'success')
    all_books = Books.query.all()
    return render_template("index.html" , data = all_books)



@admin.route("/add_auth" , methods=['POST' , 'GET'])
def add_auth():
    form = AddAuth(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        des = form.des.data
        country = form.country.data

        new_auth = Auth(name=name , des=des , county = country)

        db.session.add(new_auth)
        db.session.commit()
        flash('New Author added successfly', 'success')

        form.name.data  = ""
        form.des.data = ""
        form.country.data = ""

    return render_template('add_auth.html' , form=form , title="Add Author")



@admin.route("/<int:auth_id>/update_auth", methods=['GET', 'POST'])
def update_auth(auth_id):
    auth = Auth.query.get_or_404(auth_id)
    form = AddAuth(request.form)
 

    if request.method == 'POST' and form.validate():
        auth.name = form.name.data
        auth.des = form.des.data
        auth.county = form.country.data
        db.session.commit()
        flash('Book updeded successfly', 'success')

    form.name.data =  auth.name
    form.des.data = auth.des
    form.country.data = auth.county

    return  render_template('add_auth.html' , form=form ,  title='Update Author')
   

@admin.route("/<int:auth_id>/auth_delete" , methods=["GET" , "POST"])
@requires_auth('post:delete')
def auth_delete(payload, auth_id):
    auth = Auth.query.get_or_404(auth_id)
    db.session.delete(auth)
    db.session.commit()
    flash('Author deleted!', 'success')
    all_auth = Auth.query.all()
    return render_template("auth.html" , data=all_auth)
 
@admin.route("/authors" , methods=['GET' , 'POST'])
def authors():
    all_auth = Auth.query.all()
    return render_template("auth.html" , data=all_auth)
  