import tensorflow as tf



class Identity(tf.keras.Model):
    """ Helper module that stores the current tensor. Useful for accessing by name."""

    def call(self, x, **kwargs):
        return x

    def compute_output_shape(self, input_shape):
        return input_shape