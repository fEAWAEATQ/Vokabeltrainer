from sqlalchemy.exc import IntegrityError 
from database.Models import Vocabulary
from database.db import db
from database.user import get_user_id
from database.lesson import get_lesson_id
def get_vocab(word_foreign,username,lesson_name): #Returns all Data from the Vocabulary with the fitting word_foreign
    return Vocabulary.query.filter_by(word_foreign=word_foreign,lesson_id=get_lesson_id(lesson_name,username)).first()
def create_vocab(word_foreign,word_native,username,lesson_name): #Inserts a new vocabulary word into the database
    try:
        vocab=Vocabulary(word_foreign=word_foreign,word_native=word_native,vocab_phase=0,lesson_id=get_lesson_id(lesson_name,username))
        db.session.add(vocab)
        db.session.commit()
        return vocab
    except IntegrityError:
        db.session.rollback()
        return None

def add_vocab(word_foreign,word_native,username,lesson_name):#Adds a vocabulary word to the vocabulary Database if the word does not exists yet
    vocab=create_vocab(word_foreign,word_native,username,lesson_name)
    if vocab:
        print(f"Vocabulary word {word_foreign} created successfully.")
        return True
    else:
        print(f"Vocabulary word {word_foreign} already exists. or user {username} does not exist.")
        return False
def get_all_vocab(): #Returns all vocabulary words from the vocabulary Database
    return Vocabulary.query.all()

def delete_vocab(word_foreign,username,lesson_name) ->bool:#Deletes the selected vocabulary word, returns true if successful else false
    vocab=get_vocab(word_foreign,username,lesson_name)
    if vocab is None:
        return False
    try:
        db.session.delete(vocab)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False
#alter vocabulary word phase