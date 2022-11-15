#!/usr/bin/python3
#M1mac
import rospy
from std_msgs.msg import String

import os
import sys
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append('../..')
from robotics6.msg import Call_timer

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def timer_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I received %s", data.data)

def callback_original(data):
    rospy.loginfo(data)

rospy.init_node('listener', anonymous=True)
sub = rospy.Subscriber('chatter', String, callback)
sub_timer = rospy.Subscriber('call_timer', String, timer_callback)
sub_original = rospy.Subscriber('call_timer_original', Call_timer, callback_original)
rospy.spin()