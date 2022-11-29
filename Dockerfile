FROM tiryoh/ros-desktop-vnc:noetic


## Timezone
RUN RUN apt-get update && apt-get install -y locales && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8

##### UTC #####
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
	vim \
	wget \
	unzip \
	git \
	build-essential \
	tmux

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

RUN apt-get install -y ros-noetic-teleop-twist-keyboard ros-noetic-gmapping ros-noetic-map-server ros-noetic-amcl ros-noetic-move-base

RUN cd /home/ubuntu/ros_catkin_ws/src && \
		cd /home/ubuntu/ros_catkin_ws/src && \
        git clone https://github.com/Hibiki1020/m2_robotics.git && \
		git clone https://github.com/yuu31/stage_costom.git && \
        cd /home/ubuntu/ros_catkin_ws && \
		/bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"


WORKDIR /home/ros_catkin_ws/