import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash



def get_connection():# Returns the connection to the User Database in sqlite3 Row format.
    conn = sqlite3.connect(str(USERS_DB))
    conn.row_factory = sqlite3.Row
    return conn
    

def get_user(username): #Returns all Data from the user with the fitting username
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?',(username,))
        return cursor.fetchone()
def create_user(username,password,rank=0): #Inserts a new user into the uses Database
    pw_hash = generate_password_hash(password)
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO users (username,password,rank) VALUES (?,?,?)''',(username,pw_hash,rank))
        conn.commit()

def add_user(username,password,rank=0):#Adds a user to the users Database if the user does not exists yet
    try:
        create_user(username, password, rank)
        print(f"User {username} created")
    except sqlite3.IntegrityError:
        print(f"User {username} already exists")


def get_all_users(): #Returns all users from the users Database
    with get_connection() as conn:
        return conn.execute("SELECT * FROM users").fetchall()
    
def delete_user(username) ->bool:#Deletes the selected user, returns true if successful else false
    with get_connection() as conn:
        cur= conn.execute('DELETE FROM users WHERE username=?',(username,))
        return cur.rowcount>0 #Returns true if at least one row was deleted
    
def alter_user_rank(username: str, new_rank: int) -> bool:# Alters the rank of the selected user, returns true if successful else false
    if not isinstance(new_rank, int):
        raise TypeError("new_rank must be an int")
    with get_connection() as conn:
        cur = conn.execute('UPDATE users SET rank=? WHERE username=?', (new_rank, username))
        return cur.rowcount > 0


def alter_user_password(username, new_password) -> bool:# Alters the password of the selected user, returns true if successful else false
    pw_hash = generate_password_hash(new_password)
    with get_connection() as conn:
        cur = conn.execute('UPDATE users SET password=? WHERE username=?', (pw_hash, username))
        return cur.rowcount > 0


def alter_user_username(username, new_username)-> bool:# Alters the username of the selected user, returns true if successful else false
    if get_user(new_username) is not None:
        raise ValueError("Username already exists")
    with get_connection() as conn:
        cur=conn.execute("UPDATE users SET username=? WHERE username=?",(new_username,username))
        return cur.rowcount>0