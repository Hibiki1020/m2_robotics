#!/usr/bin/python3
#M1mac
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


if __name__ == '__main__':
    rospy.init_node("timer", anonymous=True)
    pub = rospy.Publisher("/timer", String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        time = str(rospy.get_time())
        pub.publish(time)
        rate.sleep()