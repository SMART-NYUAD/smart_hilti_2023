#!/usr/bin/env python

import sys
import rospy
import tf
import geometry_msgs.msg

def output_writer():
    rospy.init_node("output_writer")

    odom, base = sys.argv[1], sys.argv[2]
    filename = sys.argv[3]
    f = open(filename, "w")
    
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(odom, base, rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("Can't find {} to {} transform".format(odom, base))
            continue 

        f.write("{} {} {} {} {} {} {} {}\n".format(
            rospy.Time.now().to_sec(),
            trans[0],
            trans[1],
            trans[2],
            rot[0],
            rot[1],
            rot[2],
            rot[3]
        ))
        print("{}, {}, {}, {}, {}, {}, {}, {}\n".format(
            rospy.Time.now().to_sec(),
            trans[0],
            trans[1],
            trans[2],
            rot[0],
            rot[1],
            rot[2],
            rot[3]
        ))
        rate.sleep()
    f.close()


if __name__=="__main__":
    output_writer()