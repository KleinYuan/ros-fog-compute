#!/usr/bin/env bash

echo "Downloading pre-trained models ..."
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_resnet_v2_atrous_coco_11_06_2017.tar.gz -O $(PWD)/graphs/graph.tar.gz

echo "Unzipping downloaded models ..."
cd graphs && tar -xvzf graph.tar.gz && rm -rf graph.tar.gz && cd ..