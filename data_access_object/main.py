from employee_data_access_object import EmployeeDao
from models import Employee

def main():
	employee_dao = EmployeeDao('employee.db')

	emp1 = Employee(employee_id=1, name="David", age=23)
	employee_dao.add_employee(emp1)

	emp2 = Employee(employee_id=2, name="John", age=34)
	employee_dao.add_employee(emp2)

	print()
	print("------------------Print all the Employees--------------------Start")

	# Print all the employees
	for employee in employee_dao.get_all_employees():
		print("Employee Id: {}\nName: {}\nAge: {}\n".format(
			employee.employee_id, employee.name, employee.age))

	print("-----------------Print all the Employees--------------------End")
	print()

	print("-----------------Get one Employee based on employee_id=1----Start")

	employee = employee_dao.get_employee(1)
	print("Employee Id: {}\nName: {}\nAge: {}\n".format(
		employee.employee_id, employee.name, employee.age))

	print("-----------------Get one Employee based on employee_id=1----End")
	print()

	print("-----------------Update Employee based on employee_id=1----Start")

	emp1.name = "Rohan"
	employee_dao.update_employee(emp1)

	print("-----------------UpdateEmployee based on employee_id=1----End")
	print()

	print("-----------------Delete Employees---------------------Start")

	employee_dao.delete_employee(1)
	employee_dao.delete_employee(2)

	print("-----------------Delete Employees----------------------End")
	print()


if __name__ == '__main__':
	main()