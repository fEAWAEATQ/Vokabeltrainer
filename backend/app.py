from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.routes.auth import auth_routes
from backend.routes.vocab_routes import vocab_routes
from backend.database.db import db
import os

from backend.database.user import User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(auth_routes, url_prefix="/api/auth")#Registration of auth routes blueprint
app.register_blueprint(vocab_routes, url_prefix="/api")#Registration of vocab routes blueprint

def create_test_user():
    if not User.query.filter_by(username="test").first():
        user = User(
            username="test",
            password=generate_password_hash("test")
        )
        db.session.add(user)
        db.session.commit()
        print("Test user created")


with app.app_context():
    db.create_all()  # Create tables for all models
    create_test_user()  # Create a test user if not exists