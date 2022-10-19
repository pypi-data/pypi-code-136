import numpy as np


def reshape_inputs(feature: np.ndarray,
                   truth: np.ndarray = None,
                   batch_size: int = None,
                   timesteps: int = 0,
                   flatten: bool = False,
                   add1ch: bool = False) -> (np.ndarray, np.ndarray, tuple, int, np.ndarray, str):
    """Check SonusAI feature and truth data and reshape feature of size frames x strides x bands into
    one of several options:

    If timesteps > 0: (i.e. for recurrent NNs):
      no-flatten, no-channel:   sequences x timesteps x strides       x bands     (4-dim)
      flatten, no-channel:      sequences x timesteps x strides*bands             (3-dim)
      no-flatten, add-1channel: sequences x timesteps x strides       x bands x 1 (5-dim)
      flatten, add-1channel:    sequences x timesteps x strides*bands         x 1 (4-dim)

    If batch_size is None, then do not reshape; just calculate new input shape and return.

    If timesteps == 0, then do not add timesteps dimension.

    The number of samples is trimmed to be a multiple of batch_size (Keras requirement) for
    both feature and truth.
    Channel is added to last/outer dimension for channel_last support in Keras/TF.

    Returns:
      feature       reshaped feature
      truth         reshaped truth
      in_shape      input shape for model (timesteps x feature)
      num_classes   number of classes in truth = output length of nn model
      class_weights weights of each class in truth, per sklearn compute_weights()
      msg           string with report with info on data and operations done
    """
    from sonusai import SonusAIError
    from sonusai.metrics import calculate_class_weights_from_truth

    frames, strides, bands = feature.shape
    if truth is not None:
        truth_frames, num_classes = truth.shape
        # Double-check correctness of inputs
        if frames != truth_frames:
            raise SonusAIError('Frames in feature and truth do not match')
    else:
        num_classes = None

    msg = f'Feature shape={feature.shape}\n'
    if truth is not None:
        msg += f'truth shape={truth.shape}\n'
    msg += f'Reshape request: timesteps={timesteps}, batch_size={batch_size}, flatten={flatten}, add1ch={add1ch}\n'

    # Compute class weights by hand as sklearn does not handle non-existent classes
    if truth is not None:
        class_weights = calculate_class_weights_from_truth(truth)
    else:
        class_weights = None

    # Calculate new input shape only and return
    if batch_size is None:
        if flatten:
            in_shape = [strides * bands]
        else:
            in_shape = [strides, bands]

        if timesteps > 0:
            in_shape = np.concatenate(([timesteps], in_shape[0:]), axis=0)

        if add1ch:
            in_shape = np.concatenate((in_shape[0:], [1]), axis=0)

        return feature, truth, in_shape, num_classes, class_weights, msg  # quick

    if flatten:
        msg += f'Flattening {strides}x{bands} feature to {strides * bands}\n'
        feature = np.reshape(feature, (frames, strides * bands))

    # Reshape for Keras/TF recurrent models that require timesteps/sequence length dimension
    if timesteps > 0:
        sequences = frames // timesteps

        # Remove frames if remainder exists (not fitting into a multiple of new number of sequences)
        frames_rem = frames % timesteps
        batch_rem = (frames // timesteps) % batch_size
        bf_rem = batch_rem * timesteps
        sequences = sequences - batch_rem
        fr2drop = frames_rem + bf_rem
        if fr2drop:
            msg += f'Dropping {fr2drop} frames for new number of sequences to fit in multiple of batch_size\n'
            if feature.ndim == 2:
                feature = feature[0:-fr2drop, ]  # Flattened input
            elif feature.ndim == 3:
                feature = feature[0:-fr2drop, ]  # Unflattened input

            if truth is not None:
                truth = truth[0:-fr2drop, ]

        # Reshape
        msg += f'Reshape for timesteps = {timesteps}, new number of sequences (batches) = {sequences}\n'
        if feature.ndim == 2:  # Flattened input
            # str=str+'Reshaping 2 dim\n'
            feature = np.reshape(feature, (sequences, timesteps, strides * bands))  # was frames x bands*timesteps
            if truth is not None:
                truth = np.reshape(truth, (sequences, timesteps, num_classes))  # was frames x num_classes
        elif feature.ndim == 3:  # Unflattened input
            # str=str+'Reshaping 3 dim\n'
            feature = np.reshape(feature, (sequences, timesteps, strides, bands))  # was frames x bands x timesteps
            if truth is not None:
                truth = np.reshape(truth, (sequences, timesteps, num_classes))  # was frames x num_classes
    else:
        # Drop frames if remainder exists (not fitting into a multiple of new number of sequences)
        fr2drop = feature.shape[0] % batch_size
        if fr2drop > 0:
            msg += f'Dropping {fr2drop} frames for total to be a multiple of batch_size\n'
            feature = feature[0:-fr2drop, ]
            if truth is not None:
                truth = truth[0:-fr2drop, ]

    # Add channel dimension if required for input to model (i.e. for cnn type input)
    if add1ch:
        msg += 'Adding channel dimension to feature\n'
        feature = np.expand_dims(feature, axis=feature.ndim)  # add as last/outermost dim

    in_shape = feature.shape
    in_shape = in_shape[1:]  # remove frame dim size

    msg += f'Feature final shape: {feature.shape}\n'
    msg += f'Input shape final (includes timesteps): {in_shape}\n'
    if truth is not None:
        msg += f'Truth final shape: {truth.shape}\n'

    return feature, truth, in_shape, num_classes, class_weights, msg


def reshape_outputs(predict: np.ndarray,
                    truth: np.ndarray = None,
                    timesteps: int = 0) -> (np.ndarray, np.ndarray, int):
    """Reshape model output data.

    truth and predict can be either frames x num_classes, or frames x timesteps x num_classes
    In binary case, num_classes dim may not exist; detect this and set num_classes to 1.
    """
    from sonusai import SonusAIError

    if truth is not None:
        if predict.shape != truth.shape:
            raise SonusAIError('predict and truth shapes do not match')

    num_dims = predict.ndim
    dims = predict.shape

    if num_dims == 3 or (num_dims == 2 and timesteps > 0):
        if num_dims == 2:
            # 2D with timesteps - frames x timesteps
            num_classes = 1
        else:
            # 3D - frames x timesteps x num_classes
            num_classes = dims[2]

        # reshape to remove timestep dimension
        new_dims = (dims[0] * dims[1], num_classes)
        predict = np.reshape(predict, new_dims)
        if truth is not None:
            truth = np.reshape(truth, new_dims)
    else:
        if num_dims == 1:
            # 1D without timesteps - frames
            num_classes = 1

            # convert to 2D - frames x 1
            predict = np.expand_dims(predict, 1)
            if truth is not None:
                truth = np.expand_dims(truth, 1)
        else:
            # 2D without timesteps - frames x num_classes
            num_classes = dims[1]

    return predict, truth, num_classes
