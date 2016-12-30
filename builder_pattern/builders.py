from abc import ABCMeta, abstractmethod

# Robot Object

class Robot(object):
	def __init__(self):
		self.robot_head = None
		self.robot_arms = None
		self.robot_legs = None
		self.robot_torso = None

	def set_robot_head(self, head):
		self.robot_head = head

	def set_robot_torso(self, torso):
		self.robot_torso = torso

	def set_robot_arms(self, arms):
		self.robot_arms = arms

	def set_robot_legs(self, legs):
		self.robot_legs = legs


# Robot Builder Interface

class RobotBuilder:
	__metaclass__ = ABCMeta

	@abstractmethod
	def build_robot_head(self):
		pass

	@abstractmethod
	def build_robot_legs(self):
		pass

	@abstractmethod
	def build_robot_torso(self):
		pass

	@abstractmethod
	def build_robot_arms(self):
		pass

	@abstractmethod
	def get_robot(self):
		pass

# Concrete Builders

class OldRobotBuilder(RobotBuilder):
	def __init__(self):
		self.robot = Robot()

	def build_robot_head(self):
		self.robot.set_robot_head("Tin Head")

	def build_robot_legs(self):
		self.robot.set_robot_legs("Rollerskates")

	def build_robot_torso(self):
		self.robot.set_robot_torso("Tin Torso")

	def build_robot_arms(self):
		self.robot.set_robot_arms("Blowtorch Arms")	

	def get_robot(self):
		return self.robot


class EcoRobotBuilder(RobotBuilder):
	def __init__(self):
		self.robot = Robot()

	def build_robot_head(self):
		self.robot.set_robot_head("Recycled Aluminum Head")

	def build_robot_legs(self):
		self.robot.set_robot_legs("Wind Turbine Arms")

	def build_robot_torso(self):
		self.robot.set_robot_torso("Solar Powerd Torso")

	def build_robot_arms(self):
		self.robot.set_robot_arms("Super Suction Legs")	

	def get_robot(self):
		return self.robot