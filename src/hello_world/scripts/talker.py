#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
import random

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('serialIn', Int16, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        num = random.randint(0, 1024)
        hello_str = "hello world %s" % rospy.get_time()
        
        rospy.loginfo(hello_str)
        rospy.loginfo(num)
        
        pub.publish(hello_str)
        pub2.publish(num)
        
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass