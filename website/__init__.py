from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lalitbawa123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22090185:Lalit12345@csmysql.cs.cf.ac.uk:3306/c22090185_database'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_load(id):
        return User.query.get(int(id))

    return app

