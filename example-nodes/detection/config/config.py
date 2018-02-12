node = dict(
    node_name='detetcion-node',
    pub_topic='/dl/bounding-boxes',
    sub_topic='/camera/image_raw',
    queue_size=2)

dnn = dict(
    graph_fp='graphs/graph.pb',
    device='/gpu:0',
    input_tensor_name='image_tensor',
    output_tensor_name='detection_boxes'
)
