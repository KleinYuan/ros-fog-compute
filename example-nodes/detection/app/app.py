import cv2
import numpy as np
from models.node import BaseNode
from models.dnn import BaseDNN
from cv_bridge import CvBridge, CvBridgeError


class Node(BaseNode):
    def _init_processor(self):
        self.dnn = BaseDNN()
        self.bridge = CvBridge()

    def _msg_processing(self, msg):
        if not self.dnn.in_progress:
            img = self.bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            '''
            Add your pre-processing code below:
            img is the raw input from your ros topic
            and you may wanna pre process it, make it ready for deep neural network
            '''
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            height, width, _ = img.shape
            image_np_expanded = np.expand_dims(img, axis=0)

            self.dnn.predict(data=image_np_expanded)
            _res = self.dnn.get_prediction()

            '''
            Add your post processing code below:
            _res is the raw output of your deep neural network
            and you may wanna post process it
            '''

            return _res

    def _construct_pub_msg(self, _response):
        return _response


def main():
    node = Node()
    node.spin()


if __name__ == '__main__':
    main()
