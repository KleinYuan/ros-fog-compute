node = dict(
    node_name='base-node',
    pub_topic='/dl',
    sub_topic='/camera/image_raw',
    queue_size=2)

dnn = dict(
    graph_fp='graphs/graph.pb',
    device='/gpu:0',
    input_tensor_name='input',
    output_tensor_name='output'
)
