import flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_routes
from database.user import initialize_database_users, add_user,alter_user_password,alter_user_username



app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vocab.db" #Database URI for SQLAlchemy 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)#Initialize SQLAlchemy with Flask app
app.register_blueprint(auth_routes)#Registration of auth routes blueprint


if __name__ == '__main__':
    
    initialize_database_users()#Initialize all databases at start
    with app.app_context():
        db.create_all()#Create all tables in the database if they do not exist yet
    app.run()