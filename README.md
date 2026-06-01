# Vokabeltrainer

A full-stack vocabulary learning application built as a personal project for learning web development, backend architecture, authentication, database design, testing, containerization, and deployment.
Primary focus of the project was backend development, API design, authentication, database integration, testing and deployment.

The application allows users to manage lessons and vocabulary, practice words using a learning-phase system, and track learning statistics.

## Live Demo

Frontend:
https://vokabeltrainer-jcr8.onrender.com

Backend:
https://vokabeltrainer-backend.onrender.com

### Important Note

The application is hosted on Render's free tier.

After longer periods of inactivity, the backend service may enter sleep mode. Before using the application, open the backend URL once and wait until the service has fully started. Afterwards, the frontend can be used normally.

This limitation is caused by the free hosting tier and is not related to the application itself.

---

## Key Concepts

* REST API Design
* Session-based Authentication
* PostgreSQL Database Integration
* Docker Containerization
* Full-Stack Deployment
* Unit Testing

---

## Features

### User Management

* User registration
* Session-based authentication
* Login and logout functionality
* Secure password hashing using Werkzeug

### Lesson Management

* Create lessons
* Delete lessons
* List all lessons belonging to a user

### Vocabulary Management

* Add vocabulary entries to lessons
* Delete vocabulary entries
* Store vocabulary per user and lesson
* Import vocabulary entries from CSV files
   for example: house,Haus
                dog,Hund

### Learning System

* Vocabulary entries progress through learning phases
* Correct answers increase the learning phase
* Incorrect answers trigger a fallback mechanism

### Statistics

* Learning phase distribution
* Vocabulary learning statistics

### Security

* Session-based authentication
* Protected write operations (POST / DELETE)
* Passwords stored as secure hashes

### Testing

Unit tests for:

* Learning phase progression logic
* Statistics calculation
* Core business logic

Business logic is tested independently from Flask routes and database implementations.

---

## Technology Stack

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* Gunicorn
* Flask-CORS
* Werkzeug

### Frontend

* HTML5
* CSS
* Vanilla JavaScript 

### Testing

* Pytest

### Deployment

* Docker
* Docker Compose
* Render
* PostgreSQL (Render Database)

---

## API Overview

### Authentication

```http
POST /api/auth/login
POST /api/auth/logout
GET  /api/me
```

### Users

```http
POST /api/users
```

### Lessons

```http
GET    /api/users/<username>/lessons
POST   /api/users/<username>/lessons
DELETE /api/users/<username>/lessons/<lesson_name>
```

### Vocabulary

```http
GET    /api/users/<username>/lessons/<lesson_name>/vocab
POST   /api/users/<username>/lessons/<lesson_name>/vocab
DELETE /api/users/<username>/lessons/<lesson_name>/vocab/<word_foreign>
```

### Learning & Statistics

```http
POST /api/vocab/answer
GET  /api/users/<username>/stats
```

---

## Authentication

Authentication is implemented using Flask sessions.

* Users authenticate with username and password
* Passwords are securely hashed using Werkzeug
* Successful login creates a server-side session
* Session cookies are used for authenticated requests

---

## Running Locally

Before running the application locally, make sure that the frontend configuration points to the local backend instead of the deployed Render backend.

Start the application using Docker:

```bash
docker-compose up --build
```
