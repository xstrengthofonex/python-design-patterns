from employee_data_access_object import EmployeeDao
from models import Employee

import unittest

class TestDataAccessObject(unittest.TestCase):
	def setUp(self):
		self.employee_dao = EmployeeDao('employee.db')
		self.emp_1 = Employee(employee_id=1, name="Vince", age=30)
		self.employee_dao.add_employee(self.emp_1)
		self.emp_2 = Employee(employee_id=2, name="Hyeju", age=28)
		self.employee_dao.add_employee(self.emp_2)

	def test_employee_update_updates_name(self):
		self.emp_1.name = "Vincent"
		self.employee_dao.update_employee(self.emp_1)
		employee = self.employee_dao.get_employee(1)
		self.assertEqual(employee.name, "Vincent")

	def test_employee_update_updates_age(self):
		self.emp_2.age = 40
		self.employee_dao.update_employee(self.emp_2)
		employee = self.employee_dao.get_employee(2)
		self.assertEqual(employee.age, 40)

	def tearDown(self):
		self.employee_dao.delete_employee(1)
		self.employee_dao.delete_employee(2)