
class FilterChain(object):
	def __init__(self):
		self.filters = []
		self.target = None

	def add_filter(self, filter):
		self.filters.append(filter)

	def set_target(self, target):
		self.target = target

	def execute(self, request):
		for filter in self.filters:
			filter.execute(request)
		self.target.execute(request)
