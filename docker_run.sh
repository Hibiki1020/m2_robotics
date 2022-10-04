#!/bin/bash

image_name='m2_robotics'
image_tag='mac'

docker run -p 6080:80 --shm-size=1024m --privileged $image_name:$image_tag