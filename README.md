# smart_hilti_2023
Submission for the 2023 HILTI SLAM Challenge. 

## Installation
This package additionally requires ROS. 
```
git clone https://github.com/SMART-NYUAD/smart_hilti_2023.git
cd smart_hilti_2023
git submodule init
git submodule update
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
