#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Serial In: %d", data.data)

def listener():


    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("serialIn", Int16, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()