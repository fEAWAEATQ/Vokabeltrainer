from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError  
from database.models import User
from database.db import db

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
        print(f"User {username} created successfully.")
        return True
    else:
        print(f"User {username} already exists.")
        return False


def get_all_users(): #Returns all users from the users Database
    return User.query.all()
    
def delete_user(username) ->bool:#Deletes the selected user, returns true if successful else false
    user=get_user(username)
    if user is None:
        print(f"User {username} does not exist.")
        return False
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False
    
def alter_user_rank(username: str, new_rank: int) -> bool:# Alters the rank of the selected user, returns true if successful else false
    if not isinstance(new_rank, int):
        raise TypeError("new_rank must be an int")
    user= get_user(username)
    if user is None:
        return False
    try:
        user.rank=new_rank
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False
    


def alter_user_password(username, new_password) -> bool:# Alters the password of the selected user, returns true if successful else false
    pw_hash = generate_password_hash(new_password)
    user=get_user(username)
    if user is None:
        return False
    try:
        user.password=pw_hash
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False
    



def alter_user_username(username, new_username)-> bool:# Alters the username of the selected user, returns true if successful else false
    user=get_user(username)
    if user is None:
        return False
    try:
        user.username=new_username
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

def get_user_lessons(username): #Returns all lessons from the selected user
    user=get_user(username)
    if user is None:
        return []
    return user.lessons