from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError , SQLAlchemyError
from backend.database.models import User
from backend.database.db import db

def get_user(username): #Returns all Data from the user with the fitting username
    return User.query.filter_by(username=username).first()

def get_user_id(username): #Returns the id of the user with the fitting username
    user=get_user(username)
    if user:
        return user.id
    return None
def create_user(username,password,rank=0): #Inserts a new user into the uses Database
    try:
        pw_hash = generate_password_hash(password)
        user=User(username=username,password=pw_hash,rank=rank)
        db.session.add(user)
        db.session.commit()
        return user
    except IntegrityError:
        db.session.rollback()
        return None

def add_user(username,password,rank=0):#Adds a user to the users Database if the user does not exists yet
    user=create_user(username,password,rank)
    if user:
        return user
    else:
        return None


def get_all_users(): #Returns all users from the users Database
    return User.query.all()
    
def delete_user(username):#Deletes the selected user
    user=get_user(username)
    if user is None:
        return None
    try:
        db.session.delete(user)
        db.session.commit()
        return user
    except SQLAlchemyError:
        db.session.rollback()
        return None
    
def alter_user_rank(username: str, new_rank: int):# Alters the rank of the selected user
    if not isinstance(new_rank, int):
        raise TypeError("new_rank must be an int")
    user= get_user(username)
    if user is None:
        return None
    try:
        user.rank=new_rank
        db.session.commit()
        return user
    except SQLAlchemyError:
        db.session.rollback()
        return None
    

def alter_user_password(username, new_password):# Alters the password of the selected user
    pw_hash = generate_password_hash(new_password)
    user=get_user(username)
    if user is None:
        return None
    try:
        user.password=pw_hash
        db.session.commit()
        return user
    except SQLAlchemyError:
        db.session.rollback()
        return None
    


def alter_user_username(username, new_username):# Alters the username of the selected user
    user=get_user(username)
    if user is None:
        return None
    try:
        user.username=new_username
        db.session.commit()
        return user
    except SQLAlchemyError:
        db.session.rollback()
        return None

def get_user_lessons(username): #Returns all lessons from the selected user
    user=get_user(username)
    if user is None:
        return []
    return user.lessons