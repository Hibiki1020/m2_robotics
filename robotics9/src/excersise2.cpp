#include "ros/ros.h"
#include "geometry_msgs/PoseWithCovarianceStamped.h"

void amcl_pose_callback(const geometry_msgs::PoseWithCovarianceStamped::ConstPtr& msg)
{
  ROS_INFO("I heard: [%f]", msg->pose.pose.position.x);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "excercise2");
  ros::NodeHandle n;
  ros::Subscriber amcl_pose_sub = n.subscribe("amcl_pose", 1000, &amcl_pose_callback);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    ros::spinOnce();

    loop_rate.sleep();// a
  }

  return 0;
}