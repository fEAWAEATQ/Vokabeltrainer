from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_routes
from database.db import db
from database.user import add_user, get_all_users, alter_user_password, alter_user_rank, delete_user, alter_user_username, get_user_id, get_user_lessons
from database.lesson import add_lesson, delete_lesson,get_all_lessons, get_vocabularies_of_lesson
from database.vocab import add_vocab, delete_vocab, get_all_vocab
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(auth_routes)#Registration of auth routes blueprint

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Create tables for all models
        app.run()