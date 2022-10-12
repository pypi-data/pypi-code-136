import tensorflow as tf

from keras_cortex.cornet.util import Identity


class CORBlockS(tf.keras.Model):
    scale = 4  # scale of the bottleneck convolution channels

    def __init__(self, in_channels, out_channels, times=1, name=None):
        super().__init__(name=name)

        self.times = times

        self.conv_input = tf.keras.layers.Conv2D(out_channels, kernel_size=1, use_bias=False,
                                                 kernel_initializer=tf.keras.initializers.GlorotNormal())
        self.skip = tf.keras.layers.Conv2D(out_channels, kernel_size=1, strides=2, use_bias=False,
                                           kernel_initializer=tf.keras.initializers.GlorotNormal())
        self.norm_skip = tf.keras.layers.BatchNormalization()

        self.conv1 = tf.keras.layers.Conv2D(out_channels * self.scale, kernel_size=1, use_bias=False,
                                            kernel_initializer=tf.keras.initializers.GlorotNormal())
        self.nonlin1 = tf.keras.layers.ReLU()

        self.conv2 = tf.keras.layers.Conv2D(out_channels * self.scale, kernel_size=3, strides=2, use_bias=False,
                                            kernel_initializer=tf.keras.initializers.GlorotNormal())
        self.nonlin2 = tf.keras.layers.ReLU()

        self.conv3 = tf.keras.layers.Conv2D(out_channels, kernel_size=1, use_bias=False,
                                            kernel_initializer=tf.keras.initializers.GlorotNormal())
        self.nonlin3 = tf.keras.layers.ReLU()

        self.out = Identity()  # for an easy access to this block's output

        # need BatchNorm for each time step for training to work well
        for t in range(self.times):
            setattr(self, f'norm1_{t}', tf.keras.layers.BatchNormalization())
            setattr(self, f'norm2_{t}', tf.keras.layers.BatchNormalization())
            setattr(self, f'norm3_{t}', tf.keras.layers.BatchNormalization())

    def call(self, x, **kwargs):
        x = self.conv_input(x)

        for t in range(self.times):
            if t == 0:
                skip = self.norm_skip(self.skip(x))
                self.conv2.strides = (2, 2)
            else:
                skip = x
                self.conv2.strides = (1, 1)

            x = self.conv1(x)
            x = getattr(self, f'norm1_{t}')(x)
            x = self.nonlin1(x)

            x = tf.keras.layers.ZeroPadding2D((1, 1))(x)
            x = self.conv2(x)
            x = getattr(self, f'norm2_{t}')(x)
            x = self.nonlin2(x)

            x = self.conv3(x)
            x = getattr(self, f'norm3_{t}')(x)

            x += skip
            x = self.nonlin3(x)
            output = self.out(x)

        return output


def CORNetS(output_dim: int = 10):
    model = tf.keras.Sequential([
        tf.keras.Sequential([
            tf.keras.layers.ZeroPadding2D((3, 3)),
            tf.keras.layers.Conv2D(64, kernel_size=7, strides=2, use_bias=False, name='conv1',
                                   kernel_initializer=tf.keras.initializers.GlorotNormal()),
            tf.keras.layers.BatchNormalization(name='norm1'),
            tf.keras.layers.ReLU(name='nonlin1'),
            tf.keras.layers.ZeroPadding2D((1, 1)),
            tf.keras.layers.MaxPool2D(pool_size=3, strides=2, name='pool'),
            tf.keras.layers.ZeroPadding2D((1, 1)),
            tf.keras.layers.Conv2D(64, kernel_size=3, strides=1, use_bias=False, name='conv2',
                                   kernel_initializer=tf.keras.initializers.GlorotNormal()),
            tf.keras.layers.BatchNormalization(name='norm2'),
            tf.keras.layers.ReLU(name='nonlin2'),
            Identity(name='output')
        ], name='V1'),
        CORBlockS(64, 128, times=2, name='V2'),
        CORBlockS(128, 256, times=4, name='V4'),
        CORBlockS(256, 512, times=2, name='IT'),
        tf.keras.Sequential([
            tf.keras.layers.AveragePooling2D(1, name='avgpool'),
            tf.keras.layers.Flatten(name='flatten'),
            tf.keras.layers.Dense(output_dim, name='linear'),
            Identity(name="output")
        ], name='decoder')
    ])

    return model


if __name__ == '__main__':
    net = CORNetS()
    net(tf.random.normal((64, 224, 224, 3)))
