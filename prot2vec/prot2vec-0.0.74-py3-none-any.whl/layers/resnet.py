from tensorflow.keras.layers import Conv1D, Dropout, Add, Dense, BatchNormalization, Activation, Conv1DTranspose


def add_block_conv1d(x, kernel_count, kernel_size, activation, dropout):
    skip = x
    x = Conv1D(kernel_count, kernel_size, activation=activation, padding='same')(x)
    x = Dropout(dropout)(x)
    x = Conv1D(kernel_count, kernel_size, activation=activation, padding='same')(x)
    x = Add()([x, skip])
    x = Dropout(dropout)(x)

    return x


def identity_block_conv1d(x, kernel_count, kernel_size, activation, dropout):
    # copy tensor to variable called x_skip
    x_skip = x
    # Layer 1
    x = Conv1D(kernel_count, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation(activation)(x)
    x = Dropout(dropout)(x)
    # Layer 2
    x = Conv1D(kernel_count, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    # Add Residue
    x = Add()([x, x_skip])
    x = Activation('relu')(x)
    x = Dropout(dropout)(x)
    return x


def convolutional_block_conv1d(x, kernel_count, kernel_size, activation, dropout, strides):
    # copy tensor to variable called x_skip
    x_skip = x
    # Layer 1
    x = Conv1D(kernel_count, kernel_size, padding='same', strides=strides)(x)
    x = BatchNormalization()(x)
    x = Activation(activation)(x)
    x = Dropout(dropout)(x)
    # Layer 2
    x = Conv1D(kernel_count, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    # Processing Residue with conv(1,1)
    x_skip = Conv1D(kernel_count, 1, strides=strides)(x_skip)
    # Add Residue
    x = Add()([x, x_skip])
    x = Activation(activation)(x)
    x = Dropout(dropout)(x)
    return x


def deconvolutional_block_conv1d(x, kernel_count, kernel_size, activation, dropout, strides):
    # copy tensor to variable called x_skip
    x_skip = x
    # Layer 1
    x = Conv1DTranspose(kernel_count, kernel_size, padding='same', strides=strides)(x)
    x = BatchNormalization()(x)
    x = Activation(activation)(x)
    x = Dropout(dropout)(x)
    # Layer 2
    x = Conv1D(kernel_count, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    # Processing Residue with conv(1,1)
    x_skip = Conv1DTranspose(kernel_count, 1, strides=strides)(x_skip)
    # Add Residue
    x = Add()([x, x_skip])
    x = Activation(activation)(x)
    x = Dropout(dropout)(x)
    return x


def add_block_dense(x, n_neurons, activation, dropout):
    skip = x
    x = Dense(n_neurons, activation=activation, padding='same')(x)
    x = Dropout(dropout)(x)
    x = Dense(n_neurons, activation=activation, padding='same')(x)
    x = Add()([x, skip])
    x = Dropout(dropout)(x)

    return x
