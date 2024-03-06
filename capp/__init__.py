from flask import Flask
import os

application = Flask(__name__)

application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'  



from capp.carbon_app.routes import carbon_app
from capp.methodology.routes import methodology
from capp.about_us.routes import about_us
from capp.users.routes import users

application.register_blueprint(carbon_app)
application.register_blueprint(methodology)
application.register_blueprint(about_us)
application.register_blueprint(users)

