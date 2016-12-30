from front_controller import FrontController

def main():
	front_controller = FrontController()
	front_controller.dispatch_request("HOME")
	front_controller.dispatch_request("STUDENT")

if __name__ == '__main__':
	main()