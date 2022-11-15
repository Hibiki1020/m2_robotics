#!/usr/bin/python3
#M1mac
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('../')
from msg import *

if __name__ == '__main__':
    rospy.init_node("timer", anonymous=True)
    pub = rospy.Publisher("call_timer", String, queue_size=10)
    pub_original = rospy.Publisher("call_timer_original", Call_timer, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    start_time = rospy.get_time()
    interval = 10.0

    while not rospy.is_shutdown():
        time_str = String()
        original_time = Call_timer()
        original_time.word = "Hello"
        original_time.time = rospy.get_time()
        pub_original.publish(original_time)

        now = rospy.get_time()
        if(now - start_time >= interval):
            time_str.data = "time is %s [s]" % now
            pub.publish(time_str)
            start_time = now
        rate.sleep()