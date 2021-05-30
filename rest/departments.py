from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload
from models.departments import Department
from schemas.department import DepartmentSchema
from service.department_service import DepartmentService
from views import db


class DepartmentApi(Resource):
    department_schema = DepartmentSchema()

    def get(self, uuid=None):
        if not uuid:
            departments = DepartmentService.fetch_all_departments(db.session)\
                .options(joinedload(Department.employees)).all()
            return self.department_schema.dump(departments, many=True), 200
        department = DepartmentService.fetch_department_by_uuid(session=db.session, uuid=uuid)
        if not department:
            return {'message': 'No such department'}, 404
        return self.department_schema.dump(department), 200

    def post(self):
        try:
            department = self.department_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(department)
        db.session.commit()
        return self.department_schema.dump(department), 201

    def put(self, uuid):
        department = DepartmentService.fetch_department_by_uuid(session=db.session, uuid=uuid)
        if not department:
            return {'message': 'No such department'}, 404
        try:
            department = self.department_schema.load(request.json, instance=department, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(department)
        db.session.commit()
        return self.department_schema.dump(department), 200

    def delete(self, uuid):
        department = DepartmentService.fetch_department_by_uuid(session=db.session, uuid=uuid)
        if not department:
            return {'message': 'No such department'}, 404
        db.session.delete(department)
        db.session.commit()
        return {'message': 'Done'}, 204
