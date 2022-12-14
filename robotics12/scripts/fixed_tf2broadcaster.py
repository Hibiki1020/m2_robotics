#!/usr/bin/env python3
# coding: UTF-8
import geometry_msgs.msg
import rospy
import tf2_ros
import tf_conversions
import turtlesim.msg
import tf2_msgs.msg

class FixedTFBroadcaster:
    def __init__(self):
        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)

        while not rospy.is_shutdown():
            rospy.sleep(0.1)

            t = geometry_msgs.msg.TransformStamped()
            t.header.stamp = rospy.Time.now()
            t.header.frame_id = "turtle1"
            t.child_frame_id = "offset1"

            t.transform.translation.x = 0.0
            t.transform.translation.y = 2.0
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 1.0

            tfm = tf2_msgs.msg.TFMessage([t])
            self.pub_tf.publish(tfm)

if __name__ == "__main__":
    rospy.init_node("fixed_tf2_broadcaster")
    ftfb = FixedTFBroadcaster()

    rospy.spin()