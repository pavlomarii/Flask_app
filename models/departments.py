import uuid

from wsgi import db


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    employees = db.relationship('Employee', backref='department', lazy='subquery')

    def __init__(self, name, employees=None):
        self.name = name
        self.uuid = str(uuid.uuid4())
        self.employees = employees if employees else []

    def __repr(self):
        return f'Department({self.name}, {self.employees})'
