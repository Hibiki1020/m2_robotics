#!/usr/bin/python3
#M1mac
import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse

def call_service():
    rospy.loginfo("Waiting for service")
    rospy.wait_for_service('call_me')
    try:
        service = rospy.ServiceProxy('call_me', Empty)
        responce = service()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def service_client():
    rospy.init_node('service_client')
    call_service()
    rospy.spin()

if __name__ == "__main__":
    service_client()