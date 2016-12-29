from robot_builder import OldRobotBuilder, EcoRobotBuilder
from robot_director import RobotDirector

# The builder pattern 

def main():
	robot_builder = OldRobotBuilder()

	robot_director = RobotDirector(robot_builder)

	robot_director.make_robot()

	robot = robot_director.get_robot()

	print("Robot Head Type: %s" % (robot.robot_head))
	print("Robot Torso Type: %s" % (robot.robot_torso))
	print("Robot Arms Type: %s" % (robot.robot_arms))
	print("Robot Legs Type: %s" % (robot.robot_legs))

if __name__ == '__main__':
	main()