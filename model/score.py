# coding:utf-8

from runserver import db


class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(32))
    subject = db.Column('subject', db.String(32))
    score = db.Column('score', db.Integer)

    def __init__(self, name, subject, score):
        self.name = name
        self.subject = subject
        self.score = score
