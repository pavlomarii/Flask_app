import uuid

from wsgi import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date)
    salary = db.Column(db.Integer)
    department = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, name, birthday, salary):
        self.name = name
        self.birthday = birthday
        self.salary = salary
        self.uuid = str(uuid.uuid4())
        # self.department = department

    def __repr__(self):
        return f'Employee({self.name}, {self.birthday}, {self.salary})'
