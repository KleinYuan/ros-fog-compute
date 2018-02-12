FROM osrf/ros:kinetic-desktop-xenial

RUN apt-get  update -y && \
    apt-get install -y \
        python-rosinstall \
        python-rosinstall-generator \
        python-wstool \
        python-pip

RUN pip install --upgrade numpy
RUN pip install sklearn cython tensorflow scipy opencv-python

WORKDIR /root/ros/detection/

ENV ROS_IP=${ROS_IP}
ENV ROS_MASTER_URI=http://$(ROS_CORE_NODE_HOSTNAME):11311
ENV PYTHONPATH=.

ENTRYPOINT ["python", "app/app.py"]