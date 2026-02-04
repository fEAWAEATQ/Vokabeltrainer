from backend.database.db import db
from sqlalchemy import CheckConstraint


class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    __table_args__=(CheckConstraint('vocab_phase >=0 AND vocab_phase <= 6', name='check_vocab_phase'),db.UniqueConstraint('word_foreign', 'lesson_id', name='unique_word_per_lesson'))#Ensure vocab_phase is between 0 and 6 and word_foreign is unique per lesson
    id = db.Column(db.Integer, primary_key=True)# Primary Key
    vocab_phase=db.Column(db.Integer,nullable=False,default=0)#Phase of the vocabulary word in the learning process default 0
    word_foreign = db.Column(db.String(100), nullable=False)# Foreign word
    word_native = db.Column(db.String(200), nullable=False)# Native word
    lesson_id=db.Column(db.Integer,db.ForeignKey('lesson.id',ondelete='CASCADE'),nullable=False)#Foreign key for Lesson
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)# Primary Key
    username = db.Column(db.String(80), unique=True, nullable=False)# Username
    password = db.Column(db.String(200), nullable=False)# Hashed Password
    rank = db.Column(db.Integer, nullable=False, default=0)# User rank for permissions
    lessons = db.relationship('Lesson', backref='user', cascade='all, delete-orphan',passive_deletes=True)  # Relationship to Lessons
class Lesson(db.Model):
    __tablename__ = 'lesson'
    __table_args__=(db.UniqueConstraint('lesson_name', 'user_id', name='unique_lesson_per_user'),)#Ensure lesson_name is unique per user
    id=db.Column(db.Integer,primary_key=True)#Primay Key
    lesson_name=db.Column(db.String(80),nullable=False)#Lesson name
    vocabularies = db.relationship('Vocabulary', backref='lesson', cascade='all, delete-orphan',passive_deletes=True)#Relationship to Vocabulary
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)  # Foreign key to User
    