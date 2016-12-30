from abc import ABCMeta, abstractmethod

class Filter:
	__metaclass__ = ABCMeta

	@abstractmethod
	def execute(self):
		pass


class DebugFilter(Filter):
	def execute(self, request):
		print("request log: " + request)

class AuthenticationFilter(Filter):
	def execute(self, request):
		print("Authentication request: " + request)


