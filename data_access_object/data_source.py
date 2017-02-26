import sqlite3

from abc import ABCMeta, abstractmethod

class DataSource:
	__metaclass__ = ABCMeta

	@abstractmethod
	def create_connection(self):
		pass

class DataSource(DataSource):
	def __init__(self, dbname):
		self.dbname = dbname
		self.connection = None

	def create_connection(self):
		self.connection = sqlite3.connect(self.dbname)
		return self.connection

