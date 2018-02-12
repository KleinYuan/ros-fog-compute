import tensorflow as tf
from config.config import dnn as config


class BaseDNN(object):
    def __init__(self):
        self.graph_fp = config['graph_fp']
        self.input_tensor_name = config['input_tensor_name']
        self.output_tensor_name = config['output_tensor_name']
        self.in_progress = False

        self.graph = None
        self.input_tensor = None
        self.output_tensor = None
        self.prediction = None
        self.session = None

        with tf.device('{}'.format(config['device'])):
            self._load_graph()
            self._init_predictor()

    def _load_graph(self):
        self.graph = tf.Graph()
        with self.graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.graph_fp, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        tf.get_default_graph().finalize()

    def _init_predictor(self):
        tf_config = tf.ConfigProto(device_count={'gpu': 0})
        tf_config.gpu_options.allow_growth = True
        with self.graph.as_default():
            self.session = tf.Session(config=tf_config, graph=self.graph)
            self.input_tensor = self.graph.get_tensor_by_name('%s:0' % self.input_tensor_name)
            self.output_tensor = self.graph.get_tensor_by_name('%s:0' % self.output_tensor_name)

    def predict(self, data):
        self.in_progress = True
        self.prediction = None
        with self.graph.as_default():
            _prediction = self.session.run(
                self.output_tensor,
                feed_dict={
                    self.input_tensor: data
                })
            self.prediction = _prediction

        self.in_progress = False

    def get_prediction(self):
        return self.prediction

    def get_status(self):
        return self.in_progress

    def kill_predictor(self):
        self.session.close()
        self.session = None
        self.prediction = None