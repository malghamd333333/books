from app import db

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    des = db.Column(db.String(100))
    county = db.Column(db.String(100))
    books = db.relationship('Books', backref='book', lazy=True)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    title = db.Column(db.String(100))
    des = db.Column(db.String(100))
    page = db.Column(db.String())
    pub_year = db.Column(db.String())
    Auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'), nullable=False)



db.create_all()