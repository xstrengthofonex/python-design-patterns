from filters import DebugFilter, AuthenticationFilter
from filter_manager import FilterManager
from target import Target

class Client(object):
	def __init__(self):
		self.filter_manager = None

	def send_request(self, request):
		self.filter_manager.filter_request(request)

	def set_filter_manager(self, filter_manager):
		self.filter_manager = filter_manager

def main():
	filter_manager = FilterManager(Target())
	filter_manager.set_filter(AuthenticationFilter())
	filter_manager.set_filter(DebugFilter())

	client = Client()
	client.set_filter_manager(filter_manager)
	client.send_request("HOME")

if __name__ == '__main__':
	main()