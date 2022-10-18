#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

rospy.init_node('listener', anonymous=True)
sub = rospy.Subscriber('chatter', String, callback)
rospy.spin()