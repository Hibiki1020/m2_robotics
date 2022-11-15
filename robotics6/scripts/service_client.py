#!/usr/bin/python3
#M1mac
import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse
from robotics6.srv import Timer

def call_service():
    rospy.loginfo("Waiting for service")
    rospy.wait_for_service('call_me')
    try:
        service = rospy.ServiceProxy('call_me', Empty)
        responce = service()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def call_timer_service():
    rospy.loginfo("Waiting for service")
    rospy.wait_for_service('timer')
    try:
        timer_service = rospy.ServiceProxy('timer', Timer)
        current_time = rospy.get_time()
        timer_responce = timer_service(current_time)
        if timer_responce.received:
            rospy.loginfo("Timer service called")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def service_client():
    rospy.init_node('service_client')
    call_service()
    call_timer_service()
    rospy.spin()

if __name__ == "__main__":
    service_client()