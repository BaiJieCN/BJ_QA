#encoding: utf-8

from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userid = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_timestamp = db.Column(db.DateTime,default=datetime.now)
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    creator = db.relationship('User',backref=db.backref('question'))

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    answer_timestamp = db.Column(db.DateTime,default=datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    answer_creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    question = db.relationship('Question',backref=db.backref('answers',order_by=answer_timestamp.desc))
    answer_creator = db.relationship('User',backref=db.backref('answers'))