#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

rospy.init_node("tracker_publisher", anonymous=True)
pub = rospy.Publisher("camera/image_raw", Image, queue_size=10)
rate = rospy.Rate(35)

def main():
    path = "/home/leonardo/slam/"
    video_capture = cv2.VideoCapture(path + 'driverless_scenario.avi')

    while not rospy.is_shutdown():
        ret, frame = video_capture.read()
        frame = cv2.resize(frame, (640,360), fx=0.5,fy=0.5)        
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
        rate.sleep()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


cv2.waitKey(0)
cv2.destroyAllWindows()