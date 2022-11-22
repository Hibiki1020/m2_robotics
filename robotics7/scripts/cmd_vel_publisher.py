#!/usr/bin/python3
#M1mac
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class ROSNode:
    def __init__(self):
        rospy.init_node('excercise7_1', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # self.sub = rospy.Subscriber('/base_pose_ground_truth', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)

        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 2.0
        self.cmd_vel.angular.z = 1.0

        # self.pose_data = Pose()

        self.counter = 0

    # def pose_callback(self, data):
    #     self.pose_data = data

    #     if (self.pose_data.x > 9.5 or self.pose_data.x < 2.0)  or (self.pose_data.y > 9.5 or self.pose_data.y < 2.0):
    #         self.cmd_vel.linear.x = 0.3
    #         self.cmd_vel.angular.z = 2.0
    #         #print("I'm at the edge!")
    #         #print(self.pose_data)
    #         self.counter += 1
    #         if self.counter > 10:
    #             self.cmd_vel.linear.x = 0.8
    #             self.cmd_vel.angular.z = 3.0
    #         if self.counter > 20:
    #             self.cmd_vel.linear.x = 1.0
    #             self.cmd_vel.angular.z = 3.0
    #         if self.counter > 100:
    #             self.cmd_vel.linear.x = 1.5
    #             self.cmd_vel.angular.z = -3.0
    #     else:
    #         self.cmd_vel.linear.x = 2.0
    #         self.cmd_vel.angular.z = 0.0
    #         self.counter = 0

    def spin(self):
        while not rospy.is_shutdown():
            self.rate.sleep()
            self.pub.publish(self.cmd_vel)

if __name__ == '__main__':
    rosnode = ROSNode()
    rosnode.spin()