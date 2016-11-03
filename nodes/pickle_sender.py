#!/usr/bin/env python
import rospy
from ros_pickle.msg import Pickle

import os

import pickle

class TestClass():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def fancy_print(self):
        print "Variables: {}, {}, {}".format(self.a, self.b, self.c)

if __name__ == "__main__":
    rospy.init_node("test_pub")

    pub = rospy.Publisher("pickle", Pickle, queue_size=10)

    t = TestClass(1, "blah", 9.0)

    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + __file__

    class_to_send = pickle.dumps(t)

    pic_msg = Pickle(abs_path=dir_path, class_name=t.__class__.__name__, pickle=class_to_send)

    while not rospy.is_shutdown():
        pub.publish(pic_msg)
        rospy.loginfo("Sending!")
        rospy.sleep(1)