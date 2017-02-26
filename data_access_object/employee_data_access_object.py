from data_source import DataSource
from models import Employee

class EmployeeDao(object):
	def __init__(self, dbname):
		self.data_source = DataSource(dbname)
		self.connection = self.data_source.create_connection()

	def get_all_employees(self):
		employee_list = []
		query = "SELECT * FROM employees"

		with self.connection as conn:
			cursor = conn.cursor()
			for row in cursor.execute(query):
				employee = Employee(*row)
				employee_list.append(employee)

		return employee_list

	def add_employee(self, employee):
		sql = "INSERT INTO employees VALUES (?,?,?)"
		with self.connection as conn:
			cursor = conn.cursor()
			cursor.execute(sql, (employee.employee_id, employee.name, employee.age))
			print("Record is inserted into employees table for employee: {}".format(employee.name))


	def get_employee(self, employee_id):
		query = "SELECT * FROM employees WHERE employee_id=?"
		employee = None

		with self.connection as conn:
			cursor = conn.cursor()
			for row in cursor.execute(query, (employee_id,)):
				# employee_id should be unique
				if employee is None:
					employee = Employee(*row)
			
		return employee

	def update_employee(self, employee):
		sql = "UPDATE employees SET name=?, age=? WHERE employee_id=?"
		with self.connection as conn:
			cursor = conn.cursor()
			cursor.execute(sql, (employee.name, employee.age, employee.employee_id))
			print("Record is updated into employees table for employee: {}".format(employee.name))


	def delete_employee(self, employee_id):
		sql = "DELETE FROM employees WHERE employee_id=?"
		with self.connection as conn:
			cursor = conn.cursor()
			cursor.execute(sql, (employee_id,))
			print("Record is deleted from employees table for employee_id: {}".format(employee_id))
