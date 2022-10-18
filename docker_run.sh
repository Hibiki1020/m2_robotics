#!/bin/bash
image_name='m2_robotics'
image_tag='mac'

docker run -p 6080:80  \
    --rm \
    --shm-size=1024m \
    --privileged \
    $image_name:$image_tag \
    bash -c "cd /home/ubuntu/ros_catkin_ws/src/$image_name && git pull && roscd && catkin_make && bash"