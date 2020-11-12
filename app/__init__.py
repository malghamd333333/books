from flask import Flask , jsonify , session , url_for , redirect
from flask import Blueprint , render_template
from flask_sqlalchemy import SQLAlchemy

from werkzeug.exceptions import HTTPException
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from functools import wraps
import json
from os import environ as env
import app.constants
import http.client


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_CALLBACK_URL = env.get(constants.AUTH0_CALLBACK_URL)
AUTH0_CLIENT_ID = env.get(constants.AUTH0_CLIENT_ID)
AUTH0_CLIENT_SECRET = env.get(constants.AUTH0_CLIENT_SECRET)
AUTH0_DOMAIN = env.get(constants.AUTH0_DOMAIN)
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = env.get(constants.AUTH0_AUDIENCE)
 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_proj.sqlite'
db = SQLAlchemy(app)
app.secret_key = constants.SECRET_KEY
app.debug = True




@app.errorhandler(Exception)
def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response


oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=AUTH0_BASE_URL,
    access_token_url=AUTH0_BASE_URL + '/oauth/token',
    authorize_url=AUTH0_BASE_URL + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)



from app.main.routes import main
from app.admin.routes import admin
 
app.register_blueprint(main)
app.register_blueprint(admin)



def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if constants.PROFILE_KEY not in session:
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated


@app.route("/test")
def test():
    return "TEST1"


@app.route("/test2")
@requires_auth
def test2():
    return "TEST2"



@app.route('/callback')
def callback_handling():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()


    session[constants.JWT_PAYLOAD] = userinfo
    session[constants.PROFILE_KEY] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': "userinfo['picture']"
    }
    session['name'] = userinfo['name']
    return redirect(url_for('main.index'))


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri="http://localhost:5000/callback", audience="")


@app.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('main.index', _external=True), 'client_id': AUTH0_CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))
