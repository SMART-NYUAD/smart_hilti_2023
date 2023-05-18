# smart_hilti_2023
This repository details all the attempted solutions and the eventual submission to the 2023 HILTI Challenge.
## Bag Files
The bag files can be downloaded from the challenge website:

[https://hilti-challenge.com/dataset-2023.html](https://hilti-challenge.com/dataset-2023.html)

Place them in the **smart_hilti_2023/src/hilti/bag** folder before building if you are using them. 

**Note:** If you are not using Docker, then the following advice may be useful.

Since the bag files tend to be large, we recommend using symbolic links instead. To set them up, download a bag file to a folder where you'd like to keep them. Then, do the following:

```
cd smart_hilti_2023/src/hilti/bag
ln -s ~/<path to folder with bag files>/site* .
```
If you had downloaded them to the *Downloads* folder, then the second command will be: 
```
ln -s ~/Downloads/site* .
```
Note that the **site\*** portion will make the command only create links for files that start with "site", which is the case for all the bag files. 

## Installation
The package is tested on ROS Melodic running on Ubuntu 18.04. To build from source, follow the steps below. **Skip this section and go straight to the docker section if you are not using Ubuntu 18.04**

Install dependencies. 
```
sudo apt-get update 

#hdl_graph_slam
sudo apt-get -y install autoconf libtool
sudo apt-get -y install ros-melodic-geodesy ros-melodic-pcl-ros ros-melodic-nmea-msgs ros-melodic-libg2o

#fast_lio
sudo apt -y install libpcl-dev
sudo apt -y install libeigen3-dev
sudo add-apt-repository ppa:borglab/gtsam-release-4.0
sudo apt update
sudo apt install libgtsam4 libgtsam-dev libgtsam-unstable4 libgtsam-unstable-dev
sudo apt-get install cmake
sudo apt-get install libgoogle-glog-dev libgflags-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libsuitesparse-dev

#Ceres solver (for fast_lio)
wget http://ceres-solver.org/ceres-solver-2.1.0.tar.gz
tar zxf ceres-solver-2.1.0.tar.gz
cd ceres-solver-2.1.0
mkdir build
cd build
cmake ..
sudo make install

#g2o (for fast_lio). You may need to update cmake for this depending on your system. 
git clone https://github.com/RainerKuemmerle/g2o.git
cd g2o
mkdir build
cd build
cmake ..
sudo make install

#catkin build
sudo apt -y install python3-pip
sudo pip3 install -U catkin_tools
```
Clone the repository
```
git clone --recurse-submodules https://github.com/SMART-NYUAD/smart_hilti_2023.git
```
If you are using bag files, place them in the **smart_hilti_2023/src/hilti/bag** folder before proceeding
```
cd smart_hilti_2023
rosdep install --from-paths src --ignore-src -r -y
catkin build
source devel/setup.bash
```

## Docker
Alternatively, package can be executed using docker. Follow the steps below to execute. 

Install docker
[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

Afterwards, execute the following. Note that for linux distributions, docker commands may need to be executed with administrative privileges (e.g. **sudo docker ...** instead of **docker ...**)
```
git clone --recurse-submodules https://github.com/SMART-NYUAD/smart_hilti_2023.git
```
If you are using bag files, place them in the **smart_hilti_2023/src/hilti/bag** folder before proceeding
```
cd smart_hilti_2023
docker build -t smart_hilti:1.0 -f Docker/Dockerfile .
docker compose -f Docker/docker-compose.yaml up
```
With this, the docker container should be running. To execute commands, create a new terminal (but keep this current one running). In a new terminal, execute the following
```
docker exec -it smart_hilti bash
```
This gives you another terminal that has access to the existing docker container. In case you need another terminal for the container, simply repeat the command in another terminal window.  

## Usage

### hdl_graph_slam
For testing hdl_graph_slam with the handheld dataset, execute the following:
```
roslaunch hilti hdl_handheld.launch
```
Or for the robot dataset, execute the following instead:
```
roslaunch hilti hdl_robot.launch
```

### Fast_lio
Fast_lio is not yet implemented for the robot dataset. For the handheld data, execute the following:
```
roslaunch hilti fastlio_handheld.launch
```

## Publishing Transformations and Output File
In another terminal window, launch the following to publish the measured transformation. In this case, hdl_graph_slam uses **odom** and **base_link**. For fast_lio, use **camera_init** and **body** instead. 
```
rosrun tf tf_echo odom base_link
```

Note that running the launch file above will automatically register the transformations to files in the **out** folder. After processing all the bag files, simply compress the **out** folder into a zip file for submission. 
