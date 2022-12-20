#!/bin/bash
script_dir=$(cd $(dirname $0); pwd)

roslaunch robotics11 excercise5.launch

sleep 5s

rosbag record -a