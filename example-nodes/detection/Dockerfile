FROM osrf/ros:kinetic-desktop-xenial

RUN apt-get  update -y && \
    apt-get install -y \
        python-rosinstall \
        python-rosinstall-generator \
        python-wstool \
        python-pip \


RUN pip install numpy sklearn cython tensorflow scipy
