from flask import Flask
from flask import Blueprint , render_template
from flask_sqlalchemy import SQLAlchemy

from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_proj.sqlite'
db = SQLAlchemy(app)

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='KaX7yLIzgIC8UD6Iq0LBA0Zn77ZqP9Y1',
    client_secret='5iDhrspUNEEN0Tgg9RrCr8IPSuoxNYFaIXlbpYuDb55kmDLRTCHH8XwYkqz6koPL',
    api_base_url='https://mom-test1.eu.auth0.com',
    access_token_url='https://mom-test1.eu.auth0.com/oauth/token',
    authorize_url='https://mom-test1.eu.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


from app.main.routes import main
from app.admin.routes import admin
 
app.register_blueprint(main)
app.register_blueprint(admin)

