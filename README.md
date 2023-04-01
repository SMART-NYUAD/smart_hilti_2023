# smart_hilti_2023
Submission for the 2023 HILTI SLAM Challenge. 

<<<<<<< HEAD
## Docker
The package can be executed using docker. Follow the steps below to execute. 

Install docker
[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

=======
## Installation
This package additionally requires ROS. 
>>>>>>> 692909f9467403104bcae58c2d5746f971dcf240
```
git clone --recurse-submodules https://github.com/SMART-NYUAD/smart_hilti_2023.git
cd smart_hilti_2023


```

Install additional dependencies for hdl_graph_slam
```
sudo apt-get install ros-melodic-geodesy ros-melodic-pcl-ros ros-melodic-nmea-msgs ros-melodic-libg2o
sudo pip install ProgressBar2
```
Then build the workspace
```
cd smart_hilti_2023
catkin build
source devel/setup.bash
```


## Usage
For testing hdl_graph_slam, execute the following
```
roslaunch hilti hdl.launch
```
