from datetime import date

from models.departments import Department
from models.employees import Employee
from views import db


def populate():
    department1 = Department("Department1")
    department2 = Department("Department2")
    department3 = Department("Department3")
    department4 = Department("Department4")
    department5 = Department("Department5")
    employee1 = Employee("Paul", date(2000, 1, 10), 400)
    employee2 = Employee("Nika", date(2001, 2, 9), 600)
    employee3 = Employee("Alina", date(1999, 3, 8), 400)
    employee4 = Employee("John", date(1988, 4, 7), 1200)
    employee5 = Employee("Jack", date(1983, 5, 6), 520)
    employee6 = Employee("Test", date(1999, 6, 5), 888)
    employee7 = Employee("Antony", date(1984, 7, 4), 2000)
    employee8 = Employee("Ramis", date(2002, 8, 3), 1600)
    employee9 = Employee("Max", date(1992, 9, 2), 300)
    employee10 = Employee("Stepan", date(2000, 10, 1), 1600)
    department1.employees = [employee1, employee7, employee9]
    department2.employees = [employee2, employee10]
    department3.employees = [employee3]
    department4.employees = [employee4]
    department5.employees = [employee5, employee6, employee8]
    db.session.add(department1)
    db.session.add(department2)
    db.session.add(department3)
    db.session.add(department4)
    db.session.add(department5)
    db.session.add(employee1)
    db.session.add(employee2)
    db.session.add(employee3)
    db.session.add(employee4)
    db.session.add(employee5)
    db.session.add(employee6)
    db.session.add(employee7)
    db.session.add(employee8)
    db.session.add(employee9)
    db.session.add(employee10)
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print("Populating")
    populate()
    print("Successfully")
