from sqlalchemy.exc import IntegrityError 
from database.models import Lesson
from database.models import Vocabulary
from database.db import db
from database.user import get_user_id
def get_lesson(lesson_name,username): #Returns all Data from the Lesson with the fitting lesson_name
    return Lesson.query.filter_by(lesson_name=lesson_name,user_id=get_user_id(username)).first()
def get_lesson_id(lesson_name,username): #Returns the id of the lesson with the fitting lesson_name
    lesson=get_lesson(lesson_name,username)
    if lesson:
        return lesson.id
    return None
def create_lesson(lesson_name,username): #Inserts a new lesson into the database for the selected user
    try:
        lesson=Lesson(lesson_name=lesson_name,user_id=get_user_id(username))
        db.session.add(lesson)
        db.session.commit()
        return lesson
    except IntegrityError:
        db.session.rollback()
        return None
def add_lesson(lesson_name,username):#Adds a lesson to the lessons Database if the lesson does not exists yet for the selected user
    lesson=create_lesson(lesson_name,username)
    if lesson:
        print(f"Lesson {lesson_name} created successfully.")
        return True
    else:
        print(f"Lesson {lesson_name} already exists.or user {username} does not exist.")
        return False
def get_all_lessons(): #Returns all lessons from the lessons Database
    return Lesson.query.all()
def delete_lesson(lesson_name,username) ->bool:#Deletes the selected lesson, returns true if successful else false for the selected user
    lesson=get_lesson(lesson_name,username)
    if lesson is None:
        return False
    try:
        db.session.delete(lesson)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

