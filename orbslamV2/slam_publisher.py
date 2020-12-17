#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

rospy.init_node("slam_publisher", anonymous=True)

input_path = rospy.get_param("video_path")
input_name = rospy.get_param("video_name")
input_rate = rospy.get_param("rospy_rate")
height = rospy.get_param("video_height")
width = rospy.get_param("video_width")

pub = rospy.Publisher("camera/rgb/image_raw", Image, queue_size=10)
rate = rospy.Rate(input_rate)

def main():
    video_capture = cv2.VideoCapture(input_path + input_name)

    while not rospy.is_shutdown():
        ret, frame = video_capture.read()
        frame = cv2.resize(frame, (width,height))
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