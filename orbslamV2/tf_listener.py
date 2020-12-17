#!/usr/bin/env python  
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    listener.waitForTransform('/map', '/camera_link', rospy.Time(), rospy.Duration(5.0))
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/camera_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        quaternion = rot
        rpy=tf.transformations.euler_from_quaternion(quaternion)
        print('transformation between camera and camera_link detected')
        print('translation vector: (',trans[0],',',trans[1],',',trans[2],')')
        print('rotation angles: roll=',rpy[0],' pitch=',rpy[1],' yaw=',rpy[2])
        print('')


        rate.sleep()