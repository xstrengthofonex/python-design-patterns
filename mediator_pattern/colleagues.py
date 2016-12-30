
class AbstractUser(object):
	def __init__(self, mediator, name):
		self.mediator = mediator
		self.name = name

	def send(self, msg):
		raise NotImplementedError

	def receive(self, msg):
		raise NotImplementedError


class User(AbstractUser):
	def __init__(self, mediator, name):
		super(User, self).__init__(mediator, name)

	def send(self, msg):
		print(self.name + ": Sent Message: " + msg +"\n")
		self.mediator.send_message(msg, self)

	def receive(self, msg):
		print(self.name + ": Received Message: " + msg)