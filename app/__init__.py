from flask import Flask
from flask import Blueprint , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_proj.sqlite'
db = SQLAlchemy(app)


from app.main.routes import main
from app.admin.routes import admin
 
app.register_blueprint(main)
app.register_blueprint(admin)

