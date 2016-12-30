from abc import ABCMeta, abstractmethod

class FacebookGroupMediatorInterface:
	__metaclass__ = ABCMeta

	@abstractmethod
	def send_message(self, msg, user):
		pass

	@abstractmethod
	def register_user(self, user):
		pass

class FacebookGroupMediator(FacebookGroupMediatorInterface):
	def __init__(self):
		self.users = []

	def send_message(self, msg, sender):
		for user in self.users:
			if user != sender:
				user.receive(msg)

	def register_user(self, user):
		self.users.append(user)

