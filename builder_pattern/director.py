class RobotDirector(object):
	
	def __init__(self, robot_builder):
		self.robot_builder = robot_builder

	def get_robot(self):
		return self.robot_builder.get_robot()

	def make_robot(self):
		self.robot_builder.build_robot_head()
		self.robot_builder.build_robot_torso()
		self.robot_builder.build_robot_legs()
		self.robot_builder.build_robot_arms()
