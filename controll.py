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
        for vocab in get_vocabularies_of_lesson("Default Lesson","admin"):
            print(f"Admin Vocab: {vocab.word_foreign} - {vocab.word_native}")

        for lesson in get_user_lessons("admin"):
            print(f"Admin Lesson: {lesson.lesson_name}")

        for user in get_all_users():
            print(f"User: {user.username}, Rank: {user.rank}, ID: {user.id}")
        for lesson in get_all_lessons():
            print(f"Lesson: {lesson.lesson_name}, User ID: {lesson.user_id}, ID: {lesson.id}")
        for vocab in get_all_vocab():
            print(f"Vocab: {vocab.word_foreign} - {vocab.word_native}, Phase: {vocab.vocab_phase}, Lesson ID: {vocab.lesson_id}, ID: {vocab.id},")
        app.run()