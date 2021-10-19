import tensorflow as tf

print("version", tf.__version__)
try:
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
except Exception as e:
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
