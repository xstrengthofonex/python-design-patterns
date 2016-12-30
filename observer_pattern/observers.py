from abc import ABCMeta, abstractmethod
from subjects import StockGrabber

class Observer:
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self, *args, **kwargs):
		pass

class StockObserver(Observer):
	observer_id_tracker = 0

	def __init__(self, stock_grabber):
		self.observer_id = self.observer_id_tracker
		self.observer_id_tracker += 1
		self.stock_grabber = stock_grabber
		self.ibm_price = 0.0
		self.aapl_price = 0.0
		self.goog_price = 0.0
		
		print("New Observer %i was created" % self.observer_id)
		stock_grabber.register(self)

	def update(self, ibm_price, aapl_price, goog_price):
		self.ibm_price = ibm_price		
		self.aapl_price = aapl_price
		self.goog_price = goog_price
		self.print_prices()

	def print_prices(self):
		print("\nObserver %i\nIMB: %f\nAAPL: %f\nGOOG: %f\n" % (
			self.observer_id, self.ibm_price, self.aapl_price, self.goog_price))
