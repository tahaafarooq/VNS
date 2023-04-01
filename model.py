from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    number = db.Column(db.String())

    def __init__(self,id, first_name, last_name, number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}:{self.number}"


class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.String(), primary_key=True)
    numbers = db.Column(db.String())
    messages = db.Column(db.String())

    def __init__(self,id, numbers, messages):
        self.id = id
        self.numbers = numbers
        self.messages = messages

    def __repr__(self):
        return f"{self.numbers}:{self.messages}"


