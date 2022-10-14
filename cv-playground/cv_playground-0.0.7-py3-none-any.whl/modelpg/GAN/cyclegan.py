import tensorflow as tf
import tensorflow_addons as tfa
from modelpg.Helper import save_models , update_image_pool , generate_fake_samples,generate_real_samples,summarize_performance

def resnet(n_filter, input_layer):
    '''
    Residual network
    :param n_filter: number of convolutional filters to use.
    :param input_layer: Input layer for this residual layer.

    '''
    init = tf.keras.initializers.RandomNormal(stddev=0.02)

    d = tf.keras.layers.Conv2D(n_filter, (3, 3), padding='same', kernel_initializer=init)(input_layer)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    d = tf.keras.layers.Conv2D(n_filter, (3, 3), padding='same', kernel_initializer=init)(d)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.Concatenate()([d, input_layer])

    return d


def build_generator(image_shape, n_resnet=9):
    '''
    Builds the Generator for image-to-image translation
    :param image_shape: Shape of the image.
    :param n_resnet: number of resnet layers to use.
    :return: Generator model.
    '''
    init = tf.keras.initializers.RandomNormal(stddev=0.02)
    ini = tf.keras.layers.Input(shape=image_shape)

    g = tf.keras.layers.Conv2D(64, (7, 7), padding='same', kernel_initializer=init)(ini)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    g = tf.keras.layers.LeakyReLU(alpha=0.2)(g)

    g = tf.keras.layers.Conv2D(128, (3, 3), strides=(2, 2), padding='same', kernel_initializer=init)(g)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    g = tf.keras.layers.LeakyReLU(alpha=0.2)(g)

    g = tf.keras.layers.Conv2D(128, (3, 3), strides=(2, 2), padding='same', kernel_initializer=init)(g)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    g = tf.keras.layers.LeakyReLU(alpha=0.2)(g)

    for _ in range(n_resnet):
        g = resnet(256, g)

    g = tf.keras.layers.Conv2DTranspose(128, (3, 3), strides=(2, 2), padding='same', kernel_initializer=init)(g)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    g = tf.keras.layers.Activation('relu')(g)

    g = tf.keras.layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), padding='same', kernel_initializer=init)(g)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    g = tf.keras.layers.Activation('relu')(g)

    g = tf.keras.layers.Conv2D(3, (7, 7), padding='same', kernel_initializer=init)(g)
    g = tfa.layers.InstanceNormalization(axis=-1)(g)
    out_img = tf.keras.layers.Activation('tanh')(g)
    model = tf.keras.models.Model(ini, out_img)
    return model


def build_descriminator(image_shape):
    '''
    Builds Desciminator model. (patch gan)
    :param image_shape: Image Shape
    :return: Descriminator model
    '''
    # weight initializer
    init = tf.keras.initializers.RandomNormal(stddev=0.02)

    ini_sr = tf.keras.layers.Input(shape=image_shape)
    ini_tg = tf.keras.layers.Input(shape=image_shape)

    merged = tf.keras.layers.Concatenate()([ini_sr, ini_tg])

    d = tf.keras.layers.Conv2D(64, (4, 4), strides=(2, 2), padding='same', kernel_initializer=init)(merged)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    d = tf.keras.layers.Conv2D(128, (4, 4), strides=(2, 2), padding='same', kernel_initializer=init)(d)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    d = tf.keras.layers.Conv2D(256, (4, 4), strides=(2, 2), padding='same', kernel_initializer=init)(d)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    d = tf.keras.layers.Conv2D(512, (4, 4), strides=(2, 2), padding='same', kernel_initializer=init)(d)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    d = tf.keras.layers.Conv2D(512, (4, 4), padding='same', kernel_initializer=init)(d)
    d = tfa.layers.InstanceNormalization(axis=-1)(d)
    d = tf.keras.layers.LeakyReLU(alpha=0.2)(d)

    patch_out = tf.keras.layers.Conv2D(1, (4, 4), padding='same', kernel_initializer=init)(d)
    patch_out = tf.keras.layers.Activation('sigmoid')(patch_out)

    model = tf.keras.models.Model([ini_sr, ini_tg], patch_out)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
                  loss=tf.keras.losses.binary_crossentropy,
                  loss_weights=[0.5])
    return model


def composite_model(g_model_1, d_model, g_model_2, image_shape):
    '''
    Build the composite model to train each generator stepwise.
    :param g_model_1: Generator model
    :param d_model: Descriminator model for g_model_1
    :param g_model_2: Generator model
    :param image_shape: Image Shape
    :return: Composite model
    '''
    g_model_1.trainable = True
    d_model.trainable = False
    g_model_2.trainable = False

    # adversial loss
    in_sr = tf.keras.layers.Input(shape=image_shape)
    g_model_1_out = g_model_1(in_sr)
    d_out_1 = d_model([in_sr, g_model_1_out])
    # identity loss
    in_tg = tf.keras.layers.Input(shape=image_shape)
    g_out_id = g_model_1(in_tg)
    # cycle loss forward
    cycle_out_f = g_model_2(g_model_1_out)
    # cycle loss backward
    g_model_2_out = g_model_2(in_tg)
    cycle_out_b = g_model_1(g_model_2_out)

    model = tf.keras.models.Model([in_sr, in_tg], [d_out_1, g_out_id, cycle_out_f, cycle_out_b])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
                  loss=[tf.keras.losses.binary_crossentropy, 'mae', 'mae', 'mae'],
                  loss_weights=[1, 5, 10, 10])
    return model

def train_model(d_model_photo,d_model_monet,g_model_ph_mo,g_model_mo_ph,c_model_ph_mo,c_model_mo_ph,dataset,epochs=5):
    '''
    Function Used to train model
    :param d_model_photo: Descriminator for Domain A
    :param d_model_monet: Descriminator for Domain B
    :param g_model_ph_mo: Generator for Domain A (A -> B)
    :param g_model_mo_ph: Generator for Domain B (B -> A)
    :param c_model_ph_mo: Composite Model for Domain A
    :param c_model_mo_ph: Composite Model for Domain B
    :param dataset: tuple of input image and target image
    :param epochs: number of epochs to train.

    '''
    n_epoch, n_batch = epochs, 1
    # determine the patch shape of the discriminator
    patch = d_model_photo.output_shape[1]
    # load data
    trainA, trainB = dataset
    # create pool
    poolA, poolB = list(), list()
    # calculate number  of batches per training
    batch_per_epoch = int(len(trainA) / n_batch)
    n_steps = n_epoch * batch_per_epoch

    for i in range(n_steps):
        # select batch of real sample from each domain
        x_realA, y_realA = generate_real_samples(trainA, n_batch, patch)
        x_realB, y_realB = generate_real_samples(trainB, n_batch, patch)
        # select batch of fake sample from each domain
        x_fakeA, y_fakeA = generate_fake_samples(g_model_mo_ph, x_realB, patch)
        x_fakeB, y_fakeB = generate_fake_samples(g_model_ph_mo, x_realA, patch)
        # update fake images in the pool.
        x_fakeA = update_image_pool(poolA, x_fakeA)
        x_fakeB = update_image_pool(poolB, x_fakeB)

        # update generator monet -> photo via composite model
        g_loss_2, _, _, _, _ = c_model_mo_ph.train_on_batch([x_realB, x_realA], [y_realA, x_realA, x_realB, x_realA])
        # update discriminator for photo -> [real/fake]
        d_ph_loss_1 = d_model_photo.train_on_batch([x_realA, x_realB], y_realA)
        d_ph_loss_2 = d_model_photo.train_on_batch([x_realA, x_fakeB], y_fakeA)

        # update generator photo -> monet via composite model
        g_loss_1, _, _, _, _ = c_model_ph_mo.train_on_batch([x_realA, x_realB], [y_realB, x_realB, x_realA, x_realB])
        # update discriminator for monet -> [real/fake]
        d_mo_loss_1 = d_model_monet.train_on_batch([x_realB, x_realA], y_realB)
        d_mo_loss_2 = d_model_monet.train_on_batch([x_realB, x_fakeA], y_fakeB)

        print(
            f"Iteration ==========>{i + 1} \n dA [{d_ph_loss_1}, {d_ph_loss_2}]   dB [{d_mo_loss_1}, {d_mo_loss_2}] \n gA [{g_loss_1}]  gB[{g_loss_2}]")

        # summarize performance
        if (i + 1) % (batch_per_epoch * 1) == 0:
            summarize_performance(i, g_model_ph_mo, trainA, "AtoB")
            summarize_performance(i, g_model_mo_ph, trainB, "BtoA")
        if (i + 1) % (batch_per_epoch * 5) == 0:
            save_models(i, g_model_ph_mo, g_model_mo_ph)