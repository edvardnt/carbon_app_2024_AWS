from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager
application = Flask(__name__)


application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view='users.login'
login_manager.login_message_category='info'

from capp.carbon_app.routes import carbon_app
from capp.methodology.routes import methodology
from capp.about_us.routes import about_us
from capp.users.routes import users

application.register_blueprint(carbon_app)
application.register_blueprint(methodology)
application.register_blueprint(about_us)
application.register_blueprint(users)

