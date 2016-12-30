from mediators import FacebookGroupMediator
from colleagues import User

# Client

class FacebookClient(object):

	@staticmethod
	def main():
		facebook_group_mediator = FacebookGroupMediator()
		vince = User(facebook_group_mediator, "Vince")
		dave = User(facebook_group_mediator, "Dave")
		chris = User(facebook_group_mediator, "Chris")

		facebook_group_mediator.register_user(vince)
		facebook_group_mediator.register_user(dave)
		facebook_group_mediator.register_user(chris)

		dave.send("This mediator pattern is pretty cool")

if __name__ == '__main__':
	FacebookClient().main()