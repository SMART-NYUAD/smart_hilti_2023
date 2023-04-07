FROM osrf/ros:melodic-desktop-full

RUN sudo apt-get update && \ 
    sudo apt-get -y install autoconf libtool && \
    sudo apt-get -y install ros-melodic-geodesy ros-melodic-pcl-ros ros-melodic-nmea-msgs ros-melodic-libg2o && \
    sudo apt -y install python3-pip && \
    sudo pip3 install -U catkin_tools

RUN cd home \
    mkdir catkin_ws

WORKDIR /home/catkin_ws

COPY ../src src

RUN /bin/bash -c '. /opt/ros/melodic/setup.bash; cd /home/catkin_ws; catkin build;'

RUN echo "source /home/catkin_ws/devel/setup.bash" >> ~/.bashrc

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

