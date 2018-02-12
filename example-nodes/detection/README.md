# Description

This is an example ros-node,
which should be deployed to a cloud instance/cluster and connected to ROS master node.

By subscribing to live camera image view, this node can run a deep learning model against it and
publish the bounding box it detects.

### Subscribe Topic

- [X] `/camera/image_raw` [sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)

### Publish Topic

- [X] `/dl/bounding-boxes` [std_msgs/String](https://docs.ros.org/api/std_msgs/html/msg/String.html)

### Framework

- [X] Tensorflow (>= 1.0.0)

- [X] ROS Kinetic

- [X] Docker

### Deployment

1. Clone this project (detection, not entire project) into the instance you plan to deploy

2. Run `bash ./download_models.sh` to download the example frozen inference graph

3. Build docker image `make build`

4. Run container `make run`
