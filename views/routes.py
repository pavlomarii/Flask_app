from rest.employees import EmployeeApi
from rest.departments import DepartmentApi
from views import api

api.add_resource(EmployeeApi, '/employees', '/employees/<uuid>', strict_slashes=False)
api.add_resource(DepartmentApi, '/departments', '/departments/<uuid>', strict_slashes=False)
