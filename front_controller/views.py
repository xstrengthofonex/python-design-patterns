from abc import ABCMeta, abstractmethod

class View:
	__metaclass__ = ABCMeta

	@abstractmethod
	def show(self):
		pass

class HomeView(View):
	def show(self):
		print("Displaying Home Page")

class StudentView(View):
	def show(self):
		print("Displaying Student View")