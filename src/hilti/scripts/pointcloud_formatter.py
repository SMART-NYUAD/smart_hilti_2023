#! /usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
from copy import deepcopy

pub = rospy.Publisher("/velodyne_points", PointCloud2, queue_size=10)

def pointcloud_formatter():
    rospy.init_node("pointcloud_formatter")
    sub = rospy.Subscriber("/velodyne_points_raw", PointCloud2, subscriber_callback)
    rospy.spin()
    
def subscriber_callback(data):
    # data.fields[4], data.fields[5] = data.fields[5], data.fields[4]
    data.fields[5].name = "time"
    print(data.fields)
    pub.publish(data)

if __name__=="__main__":
    pointcloud_formatter()