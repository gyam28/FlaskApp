from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy() #instantiating the bookkeeper from auth init
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"

def create_app(config_type):
    app = Flask(__name__)


    configuration = os.path.join(os.getcwd(),'config',config_type+".py") #cwd = currently working directory
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.auth import auth
    from app.posts import posts

    app.register_blueprint(auth)
    app.register_blueprint(posts)

    return app
