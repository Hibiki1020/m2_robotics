#!/usr/bin/python3
#M1mac
import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse
from robotics6.srv import Timer
from robotics6.srv import TimerResponse

def handle_service(req):
    rospy.loginfo("Called!!")
    return EmptyResponse()

def timer_handler_service(req):
    rospy.loginfo("%f[s], called!", req.current_time)
    return TimerResponse(received=True)

def service_server():
    rospy.init_node('service_server')
    s = rospy.Service('call_me', Empty, handle_service)
    print("Ready to call service")
    rospy.spin()

if __name__ == "__main__":
    service_server()