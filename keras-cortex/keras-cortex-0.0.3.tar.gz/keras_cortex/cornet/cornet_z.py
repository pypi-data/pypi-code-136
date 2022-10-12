import tensorflow as tf

from keras_cortex.cornet.util import Identity


class CORBlockZ(tf.keras.Model):

    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, name=None):
        super().__init__(name=name)
        self.kernel_size = kernel_size

        self.pad1 = tf.keras.layers.ZeroPadding2D((self.kernel_size, self.kernel_size))
        self.conv = tf.keras.layers.Conv2D(out_channels, kernel_size=kernel_size, strides=stride,
                                           kernel_initializer=tf.keras.initializers.GlorotUniform(),
                                           bias_initializer=tf.keras.initializers.Constant(0))
        self.nonlin = tf.keras.layers.ReLU()
        self.pad2 = tf.keras.layers.ZeroPadding2D((1, 1))
        self.pool = tf.keras.layers.MaxPool2D(pool_size=3, strides=2)
        self.out = Identity()  # for an easy access to this block's output


    def call(self, x, **kwargs):
        x = self.pad1(x)
        x = self.conv(x)
        x = self.nonlin(x)
        x = self.pad2(x)
        x = self.pool(x)
        x = self.out(x)  # for an easy access to this block's output

        return x

    def compute_output_shape(self, input_shape):
        shape = self.pad1.compute_output_shape(input_shape)
        shape = self.conv.compute_output_shape(shape)
        shape = self.pad2.compute_output_shape(shape)
        shape = self.pool.compute_output_shape(shape)
        shape = self.out.compute_output_shape(shape)

        return shape

    def get_config(self):
        config = super(CORBlockZ, self).get_config()
        config.update({"kernel_size": self.kernel_size})
        return config


def CORNetZ(output_dim: int = 10, name="CORNetZ"):
    """CORNet Z architecture. Smaller than S, but still efficient."""

    return tf.keras.Sequential([
        CORBlockZ(3, 64, kernel_size=7, stride=2, name='V1'),
        CORBlockZ(64, 128, name='V2'),
        CORBlockZ(128, 256, name='V4'),
        CORBlockZ(256, 512, name='IT'),
        tf.keras.Sequential([
            tf.keras.layers.AvgPool2D(1, name='avgpool'),
            tf.keras.layers.Flatten(name='flatten'),
            tf.keras.layers.Dense(output_dim,
                                  kernel_initializer=tf.keras.initializers.GlorotUniform(),
                                  bias_initializer=tf.keras.initializers.Constant(0),
                                  name="output"),
        ], name='decoder')
    ], name=name)


if __name__ == '__main__':
    network = CORNetZ(output_dim=15)
    output = network(tf.random.normal((128, 128, 128, 3)))
    print(output.shape)