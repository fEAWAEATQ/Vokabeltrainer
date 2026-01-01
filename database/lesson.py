from sqlalchemy.exc import IntegrityError 
from database.models import Lesson
from database.vocab import add_vocab
from database.models import Vocabulary
from database.db import db
from database.user import get_user_id
def get_lesson(lesson_name,username): #Returns all Data from the Lesson with the fitting lesson_name
    return Lesson.query.filter_by(lesson_name=lesson_name,user_id=get_user_id(username)).first()
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


#not checked yet
def add_vocab_to_lesson(lesson_name,word_foreign,word_native,username):#Adds a vocabulary word to the selected lesson
    lesson=get_lesson(lesson_name=lesson_name,username=username)
    if not lesson:
        return False
    if Vocabulary.query.filter_by(lesson_id=lesson.id, word_foreign=word_foreign).first():
        return False
    new_vocab = add_vocab(word_foreign=word_foreign, word_native=word_native)
    lesson.vocabularies.append(new_vocab)
    db.session.add(new_vocab)
    db.session.commit()
    return True
def delete_vocab_from_lesson(lesson_name,word_foreign,username):#Deletes the selected vocabulary word from the selected lesson
    lesson=get_lesson(lesson_name=lesson_name,username=username)
    if not lesson:
        return False
    vocab=Vocabulary.query.filter_by(lesson_id=lesson.id, word_foreign=word_foreign).first()
    if not vocab:
        return False
    try:
        db.session.delete(vocab)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False