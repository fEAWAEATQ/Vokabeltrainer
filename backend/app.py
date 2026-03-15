from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.routes.auth import auth_routes
from backend.routes.vocab_routes import vocab_routes
from backend.database.db import db
import os
from backend.database.user import User
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import time
from flask_cors import CORS
load_dotenv() 

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS with support for credentials
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
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
    connect=False
    for i in range(10):
        try:
            db.create_all()  # Create tables for all models
            connect=True
            break
        except Exception as e:
            print(f"Error creating tables: {e}")
            time.sleep(3)  # Wait before retrying
    if connect:
        create_test_user()  # Create a test user if not exists