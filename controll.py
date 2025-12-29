import flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_routes




app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vocab.db" #Database URI for SQLAlchemy 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" #Database URI for SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)#Initialize SQLAlchemy with Flask app
app.register_blueprint(auth_routes)#Registration of auth routes blueprint

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()#Create all tables in the database if they do not exist yet
    app.run()