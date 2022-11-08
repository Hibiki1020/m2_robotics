#!/usr/bin/python3
#M1mac
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


if __name__ == '__main__':
    rospy.init_node('excercise1', anonymous=True)

    cmd_vel = Twist()
    cmd_vel.linear.x = 2.0
    cmd_vel.angular.z = 2.0

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(cmd_vel)
        rate.sleep()