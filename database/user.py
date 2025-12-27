import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash

# use a module-relative path so the DB file is always next to this module
USERS_DB = Path(__file__).parent / "Users.db"

def get_connection():# Returns the connection to the User Database in sqlite3 Row format.
    conn = sqlite3.connect(str(USERS_DB))
    conn.row_factory = sqlite3.Row
    return conn
def create_db_users(): # Creats the Database for the Useraccount
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            rank INTEGER DEFAULT 0
        )''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Databaseerror:{e}")
    finally:
        cursor.close()
        conn.close()

def initialize_all_databases(): #This functions initializes all Databases
    create_db_users()
    #All further Databasis will be written there

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


