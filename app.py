from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_routes
from routes.vocab_routes import vocab_routes
from database.db import db
import os
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(auth_routes)#Registration of auth routes blueprint
app.register_blueprint(vocab_routes)#Registration of vocab routes blueprint
   
with app.app_context():
    db.create_all()  # Create tables for all models