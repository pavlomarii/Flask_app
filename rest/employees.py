from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from schemas.employee import EmployeeSchema
from service.employee_service import EmployeeService
from views import db


class EmployeeApi(Resource):
    employee_schema = EmployeeSchema()

    def get(self, uuid=None):
        if not uuid:
            employees = EmployeeService.fetch_all_employees(db.session).all()
            return self.employee_schema.dump(employees, many=True), 200
        employee = EmployeeService.fetch_employee_by_uuid(session=db.session, uuid=uuid)
        if not employee:
            return {'message': 'No such employee'}, 404
        return self.employee_schema.dump(employee), 200

    def post(self):
        try:
            employee = self.employee_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(employee)
        db.session.commit()
        return self.employee_schema.dump(employee), 201

    def put(self, uuid):
        employee = EmployeeService.fetch_employee_by_uuid(session=db.session, uuid=uuid)
        if not employee:
            return {'message': 'No such employee'}, 404
        try:
            employee = self.employee_schema.load(request.json, instance=employee, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(employee)
        db.session.commit()
        return self.employee_schema.dump(employee), 200

    def delete(self, uuid):
        employee = EmployeeService.fetch_employee_by_uuid(session=db.session, uuid=uuid)
        if not employee:
            return {'message': 'No such employee'}, 404
        db.session.delete(employee)
        db.session.commit()
        return {'message': 'Done'}, 204
