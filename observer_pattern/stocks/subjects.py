from abc import ABCMeta, abstractmethod

class Subject:
	__metaclass__ = ABCMeta

	@abstractmethod
	def register(self, observer):
		pass

	@abstractmethod
	def unregister(self, observer):
		pass

	@abstractmethod
	def notify_observers(self):
		pass


class StockGrabber(Subject):

	def __init__(self):
		self.observers = []
		self.ibm_price = 0.0
		self.goog_price = 0.0
		self.aapl_price = 0.0

	def register(self, observer):
		self.observers.append(observer)
		print("Observer %i was added" % observer.observer_id)

	def unregister(self, observer):
		self.observers.remove(observer)
		print("Observer %i was deleted" % observer.observer_id)

	def notify_observers(self):
		for observer in self.observers:
			observer.update(ibm_price=self.ibm_price, 
							aapl_price=self.aapl_price, 
				            goog_price=self.goog_price)

	def set_ibm_price(self, price):
		self.ibm_price = price
		self.notify_observers()
			
	def set_goog_price(self, price):
		self.goog_price = price
		self.notify_observers()

	def set_aapl_price(self, price):
		self.aapl_price = price
		self.notify_observers()