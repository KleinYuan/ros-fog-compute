# Base Node

This node is based on tensorflow and some limitations exist for now (will be scaled in future):

- [X] Only one sub and one pub

- [X] Tensorflow checkpoint has to be frozen

- [X] Only one input and output tensor

To run it:

- [X] Obtain your frozen google protobuf model and put it under graphs folder

- [X] Modify your config/config.py to be align with yours

- [X] Export env variables of `ROS_IP`, `ROS_MASTER_URI`, `ROS_HOSTNAME` to connect to your ros master node

- [X] Run `python app/app.py` to spin up the node


# Warning

I know you may wanna just git clone this repo and run with one command to call it a day.
However, unfortunately, this base node is not something you can just run!

You need to do a little bit modifications, during the process of which I believe you can gain better
understanding of what's going on.


For lazy dudes:

Please refer to `example-nodes` and you should find what you are looking for there.

