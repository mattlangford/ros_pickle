#!/usr/bin/env python
import rospy
from ros_pickle.msg import Pickle
import pickle
import os
import imp

rospy.init_node("test_rec")

def got_msg(msg):
    # Need to import class from the other file here.

    t = pickle.loads(msg.pickle)
    t.fancy_print()

rospy.Subscriber("pickle", Pickle, got_msg, queue_size=10)
print "Listening..."
rospy.spin()