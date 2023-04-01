# smart_hilti_2023
Submission for the 2023 HILTI SLAM Challenge. 
## Bag Files
The bag files can be downloaded from the challenge website:

[https://hilti-challenge.com/dataset-2023.html](https://hilti-challenge.com/dataset-2023.html)

Place them in the **smart_hilti_2023/src/hilti/bag** folder before building if you are using them.

## Installation
The package is tested on ROS Melodic running on Ubuntu 18.04. To build from source, follow the steps below. **Skip this section and go straight to the docker section if you are not using Ubuntu 18.04**

Install dependencies. 
```
sudo apt-get update 
sudo apt-get -y install autoconf libtool
sudo apt-get -y install ros-melodic-geodesy ros-melodic-pcl-ros ros-melodic-nmea-msgs ros-melodic-libg2o
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
cd smart_hilti_2023/Docker
docker build -t smart_hilti:1.0 -f Dockerfile ..
docker-compose up
```
Create a new terminal (but keep this current one running). In a new terminal, execute the following
```
docker exec -it smart_hilti bash
source devel/setup.bash
```
With this you should have a working docker container. In case you need another terminal for the container, simply repeat the last two commands in the new terminal. 

## Usage
For testing hdl_graph_slam, execute the following
```
roslaunch hilti hdl.launch
```
