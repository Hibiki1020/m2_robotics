#!/usr/bin/python3
#M1mac
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class ROSNode:
    def __init__(self):
        rospy.init_node('excercise2', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)

        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 2.0

        self.pose_data = Pose()

    def pose_callback(self, data):
        self.pose_data = data

        if abs(self.pose_data.x) > 10.0 or abs(self.pose_data.y) > 10.0:
            self.cmd_vel.linear.x = 2.0
            self.cmd_vel.angular.z = 2.0
        else:
            self.cmd_vel.linear.x = 2.0
            self.cmd_vel.angular.z = 0.0

    def spin(self):
        while not rospy.is_shutdown():
            self.rate.sleep()
            self.pub.publish(self.cmd_vel)

if __name__ == '__main__':
    rosnode = ROSNode()
    rosnode.spin()