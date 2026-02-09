# Vokabeltrainer

A RESTful backend application for learning and managing vocabulary.
The project supports users, lessons, vocabulary entries, learning phases, and statistics, and focuses on clean backend architecture, session-based authentication, and testable business logic.

The backend is designed API-first, follows a clear separation of concerns (routes, logic, database)
Features

👤 User management

User registration

Session-based login and logout

Secure password hashing

📚 Lessons

Create and delete lessons per user

List all lessons of a user

📖 Vocabulary

Add and delete vocabulary entries per lesson

Each vocabulary entry belongs to exactly one lesson and user

🔁 Learning phase system

Vocabulary entries progress through learning phases

Correct answers increase the phase

Incorrect answers trigger a defined fallback logic

📊 Statistics

Total vocabulary count

Learned vocabulary count

Phase distribution overview

🔐 Security

Write operations (POST / DELETE) are protected by login sessions

Read-only operations (GET) are publicly accessible by design

🧪 Testing

Unit tests for core business logic (learning phases and statistics)


🛠️ Tech Stack

Python 3

Flask – web framework

Flask-SQLAlchemy – ORM and database integration

SQLite – local development database

Tools – password hashing and security utilities

Pytest – unit testing framework


🌐 API Overview

Authentication
POST /auth/login
POST /auth/logout

Users
POST /users                     # register a new user

Lessons
GET    /users/<username>/lessons
POST   /users/<username>/lessons
DELETE /users/<username>/lessons/<lesson_name>

Vocabulary
GET    /users/<username>/lessons/<lesson_name>/vocab
POST   /users/<username>/lessons/<lesson_name>/vocab
DELETE /users/<username>/lessons/<lesson_name>/vocab/<word_foreign>

Learning & Statistics
POST /vocab/answer
GET  /users/<username>/stats



🔐 Authentication & Security

Authentication is implemented using Flask sessions.

Users authenticate via username and password

Passwords are securely hashed using Werkzeug

After a successful login, the user ID is stored in the session

Write operations (POST / DELETE) require an active session

Read-only operations (GET) are publicly accessible by design

🧪 Testing

Core business logic is covered by unit tests using Pytest.

Tested components include:

Learning phase calculation logic

Vocabulary statistics aggregation

The business logic is tested independently from Flask routes and the database layer to ensure correctness and maintainability.
