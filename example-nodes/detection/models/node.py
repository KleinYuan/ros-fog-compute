#!/usr/bin/env python

import rospy
from abc import abstractmethod
from sensor_msgs.msg import Image
from config.config import node as config


class BaseNode(object):
    def __init__(self):
        self.node_name = config['node_name']
        rospy.init_node(self.node_name, anonymous=False)
        self.pub_topic = config['pub_topic']
        self.sub_topic = config['sub_topic']
        self.pub = rospy.Publisher(self.pub_topic, Image, queue_size=config['queue_size'])
        self.sub = rospy.Subscriber(self.sub_topic, Image, lambda m: self._sub_cb(m))
        self.in_process = False

    def _sub_cb(self, msg):
        if not self.in_process:
            _response = self._msg_processing(msg)
            _pub_msg = self._construct_pub_msg(_response)
            self.pub.publish(_pub_msg)

    @abstractmethod
    def _init_processor(self):
        raise NotImplementedError("_init_processor not implemented by {}".format(self.server_name))

    @abstractmethod
    def _msg_processing(self, msg):
        raise NotImplementedError("_msg_processing not implemented by {}".format(self.server_name))

    @abstractmethod
    def _construct_pub_msg(self, _response):
        raise NotImplementedError("_construct_pub_msg not implemented by {}".format(self.server_name))

    def spin(self):
        while not rospy.is_shutdown():
            self.sub.spin()
