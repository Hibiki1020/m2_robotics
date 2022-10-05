#!/bin/bash

image_name='m2_robotics'
image_tag='mac'

docker build -t $image_name:$image_tag .