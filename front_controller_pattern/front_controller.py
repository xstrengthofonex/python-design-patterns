from dispatcher import Dispatcher

class FrontController(object):
	def __init__(self):
		self.dispatcher = Dispatcher()

	def is_authenticated(self):
		print("User is authenticated sucessfully")
		return True

	def track_request(self, request):
		print("Page requested: " + request)

	def dispatch_request(self, request):
		#Log Each Request
		self.track_request(request)

		#Authenticate user
		if self.is_authenticated():
			self.dispatcher.dispatch(request)
			