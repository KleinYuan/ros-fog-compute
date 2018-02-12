node = dict(
    node_name='detetcion-node',
    pub_topic='/dl/bounding-boxes',
    sub_topic='/camera/image_raw',
    queue_size=2)

dnn = dict(
    graph_fp='graphs/faster_rcnn_inception_resnet_v2_atrous_coco_11_06_2017/frozen_inference_graph.pb',
    device='/gpu:0',
    input_tensor_name='image_tensor',
    output_tensor_name='detection_boxes'
)
