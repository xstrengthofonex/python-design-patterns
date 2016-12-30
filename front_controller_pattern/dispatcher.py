from views import HomeView, StudentView

class Dispatcher(object):
	def __init__(self):
		self.home_view = HomeView()
		self.student_view = StudentView()

	def dispatch(self, request):
		if request == "STUDENT":
			self.student_view.show()
		elif request == "HOME":
			self.home_view.show()
		else:
			print("Page Not Found")