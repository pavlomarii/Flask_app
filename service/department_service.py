from models.departments import Department


class DepartmentService:
    @staticmethod
    def fetch_all_departments(session):
        return session.query(Department)

    @classmethod
    def fetch_department_by_uuid(cls, session, uuid):
        return cls.fetch_all_departments(session).filter_by(uuid=uuid).first()
