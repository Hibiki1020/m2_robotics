FROM tiryoh/ros-desktop-vnc:noetic

RUN apt-get update && apt-get install -y \
	vim \
	wget \
	unzip \
	git \
	build-essential

RUN git config --global user.name “Hibiki1020” && \
    git config --global user.email “hibikijitaku@gmail.com”

########## ROS setup ##########
RUN mkdir -p /home/ubuntu/ros_catkin_ws/src && \
	cd /home/ubuntu/ros_catkin_ws/src && \
	/bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_init_workspace" && \
	cd /home/ubuntu/ros_catkin_ws && \
	/bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make" && \
	echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
	echo "source /home/ubuntu/ros_catkin_ws/devel/setup.bash" >> ~/.bashrc && \
	echo "export ROS_PACKAGE_PATH=\${ROS_PACKAGE_PATH}:/home/ubuntu/ros_catkin_ws" >> ~/.bashrc && \
	echo "export ROS_WORKSPACE=/home/ubuntu/ros_catkin_ws" >> ~/.bashrc
## cmk
RUN echo "function cmk(){\n	lastpwd=\$OLDPWD \n	cpath=\$(pwd) \n cd /home/ubuntu/ros_catkin_ws \n catkin_make \$@ \n cd \$cpath \n	OLDPWD=\$lastpwd \n}" >> ~/.bashrc
########## dnn_attitude_estimation ##########
##### NO cache #####
ARG CACHEBUST=1

RUN cd /home/ubuntu/ros_catkin_ws/src && \
		cd /home/ubuntu/ros_catkin_ws/src && \
        git clone https://github.com/Hibiki1020/m2_robotics.git && \
        cd /home/ubuntu/ros_catkin_ws && \
		/bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"


WORKDIR /home/ros_catkin_ws/