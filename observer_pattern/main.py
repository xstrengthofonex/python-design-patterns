from subjects import StockGrabber
from observers import StockObserver

def main():
	stock_grabber = StockGrabber()

	observer_1 = StockObserver(stock_grabber)

	stock_grabber.set_ibm_price(197.00)
	stock_grabber.set_aapl_price(676.40)
	stock_grabber.set_goog_price(677.60)

if __name__ == '__main__':
	main()