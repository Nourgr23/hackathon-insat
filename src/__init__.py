from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
import os

app = Flask(__name__)

# app.config.from_object(config("APP_SETTINGS"))

app.config["DEBUG"] = True
app.config['MAX_CONTENT_LENGTH'] = 9 * 1000 * 1000
app.config['SECRET_KEY'] = "hqdlksfjkljflqsjfkljazklrjazlker"
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join('src','db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + 'db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app,db)
mail = Mail(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

cors = CORS(app, resources={r"/product/*": {"origins": "*"}})
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
