from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from backend.database.models import Vocabulary
from backend.database.db import db
from backend.database.user import get_user_id
from backend.database.lesson import get_lesson_id
from backend.logic.vocab_phase import calculate_next_phase
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
        return vocab
    else:
        return None
def get_all_vocab(): #Returns all vocabulary words from the vocabulary Database
    return Vocabulary.query.all()

def delete_vocab(word_foreign,username,lesson_name):#Deletes the selected vocabulary word
    vocab=get_vocab(word_foreign,username,lesson_name)
    if vocab is None:
        return None
    try:
        db.session.delete(vocab)
        db.session.commit()
        return vocab
    except SQLAlchemyError:
        db.session.rollback()
        return None
def get_phase(word_foreign,username,lesson_name): #Returns the vocab_phase of the selected vocabulary word
    vocab=get_vocab(word_foreign,username,lesson_name)
    if vocab:
        return vocab.vocab_phase
    else:
        return None
def set_phase(word_foreign,username,lesson_name,answer_bool): #Sets the vocab_phase of the selected vocabulary word
    vocab=get_vocab(word_foreign,username,lesson_name)
    if vocab is None:
        return None
    try:
        vocab.vocab_phase = calculate_next_phase(vocab.vocab_phase, answer_bool)
        db.session.commit()
        return vocab
    except SQLAlchemyError:
        db.session.rollback()
        return None