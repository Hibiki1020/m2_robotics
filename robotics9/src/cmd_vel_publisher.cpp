#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cmd_vel_publisher");
  ros::NodeHandle n;
  ros::Publisher cmd_vel_pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 1000);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    geometry_msgs::Twist msg;
    msg.linear.x = 0.5;
    msg.angular.z = 0.2;

    cmd_vel_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}