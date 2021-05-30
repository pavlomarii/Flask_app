from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.employees import Employee


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
        include_fk = True
