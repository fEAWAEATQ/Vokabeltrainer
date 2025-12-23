import sqlite3
from werkzeug.security import generate_password_hash
DB_Users="Users.db"
def get_connection():# Returns the connection to the User Database in sqlite3 Row format.
    conn = sqlite3.connect(DB_Users)
    conn.row_factory = sqlite3.Row
    return conn
def Create_DB_Users(): # Creats the Database for the Useraccount
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

def Initialize_All_Databases(): #This functions initializes all Databases
    Create_DB_Users()
    #All further Databasis will be written there

def Get_User(username): #Returns all Data from the user with the fitting username
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?',(username,))
        return cursor.fetchone()
def Create_User(username,password,rank=0): #Inserts a new user into the uses Database
    pw_hash = generate_password_hash(password)
    try:
        with get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute('''INSERT INTO users (username,password,rank) VALUES (?,?,?)''',(username,pw_hash,rank))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"User {username} already exists")

def Add_User(username,password,rank=0): #Checks if the user exists if not calls the Creat_User function
    try:
        Create_User(username, password, rank)
        print(f"User {username} created")
    except sqlite3.IntegrityError:
        print(f"User {username} already exists")


