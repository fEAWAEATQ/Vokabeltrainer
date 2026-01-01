from flask_sqlalchemy import SQLAlchemy#made this file to avoid circular imports
import sqlite3
from sqlalchemy import event
from sqlalchemy.engine import Engine
db=SQLAlchemy()#Initialize SQLAlchemy without Flask app
@event.listens_for(Engine, "connect")#Enable foreign key constraint for SQLite
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()