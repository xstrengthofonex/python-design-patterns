from filter_chain import FilterChain

class FilterManager(object):
	def __init__(self, target):
		self.filter_chain = FilterChain()
		self.filter_chain.set_target(target)

	def set_filter(self, filter):
		self.filter_chain.add_filter(filter)

	def filter_request(self, request):
		self.filter_chain.execute(request)

