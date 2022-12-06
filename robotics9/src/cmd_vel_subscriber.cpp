#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

void cmd_vel_callback(const geometry_msgs::Twist::ConstPtr& msg)
{
  ROS_INFO("I heard: [%f]", msg->linear.x);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "cmd_vel_subscriber");
  ros::NodeHandle n;
  ros::Subscriber cmd_vel_sub = n.subscribe("cmd_vel", 1000, &cmd_vel_callback);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}