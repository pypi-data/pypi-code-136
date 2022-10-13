"""sonusai keras_predict

usage: keras_predict [-hvr] (-m MODEL) (-d INPUT) (-w KMODEL) [-b BATCH] [-t TSTEPS] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -m MODEL, --model MODEL         Python model file.
    -d INPUT, --input INPUT         Input data.
    -w KMODEL, --weights KMODEL     Keras model weights file.
    -b BATCH, --batch BATCH         Batch size.
    -t TSTEPS, --tsteps TSTEPS      Timesteps.
    -o OUTPUT, --output OUTPUT      Output directory.
    -r, --reset                     Reset model between each file.

Run prediction on a trained Keras model defined by a SonusAI Keras Python model file using SonusAI genft data
and/or WAV data.

Inputs:
    MODEL       A SonusAI Python model file with build and/or hypermodel functions.
    INPUT       The input data can be a file or glob of genft H5 files and/or WAV files.
    KMODEL      A Keras model weights file (or model file with weights).

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5
                        dataset:    predict
                    keras_predict.log

Results are written into subdirectory <MODEL>-<TIMESTAMP> unless OUTPUT is specified.

"""
from sonusai import logger


def main():
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    model_name = args['--model']
    input_name = args['--input']
    weights_name = args['--weights']
    batch_size = args['--batch']
    timesteps = args['--tsteps']
    output_dir = args['--output']
    reset = args['--reset']

    from os import makedirs
    from os.path import basename
    from os.path import exists
    from os.path import join
    from os.path import splitext

    import h5py
    import keras2onnx
    import keras_tuner as kt
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras import backend as kb

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.data_generator import SequenceFromH5
    from sonusai.data_generator.utils import get_frames_per_batch
    from sonusai.mixture import get_feature_from_audio
    from sonusai.mixture import read_audio
    from sonusai.utils import braced_glob
    from sonusai.utils import check_keras_overrides
    from sonusai.utils import create_ts_name
    from sonusai.utils import import_keras_model
    from sonusai.utils import reshape_inputs
    from sonusai.utils import reshape_outputs

    model_base = basename(model_name)
    model_root = splitext(model_base)[0]

    if batch_size is not None:
        batch_size = int(batch_size)

    if timesteps is not None:
        timesteps = int(timesteps)

    if output_dir is None:
        output_dir = create_ts_name(model_root)

    makedirs(output_dir, exist_ok=True)

    # Setup logging file
    create_file_handler(join(output_dir, 'keras_predict.log'))
    update_console_handler(verbose)
    initial_log_messages('keras_predict')

    logger.info(f'TF ver: {tf.__version__}')
    logger.info(f'Keras ver: {tf.keras.__version__}')
    logger.info(f'Keras2onnx ver: {keras2onnx.__version__}')
    logger.info('')

    # Import model definition file
    logger.info(f'Importing {model_base}')
    model = import_keras_model(model_name)
    with h5py.File(weights_name, 'r') as f:
        feature = f.attrs['sonusai_feature']
        num_classes = int(f.attrs['sonusai_num_classes'])

    # Check overrides
    timesteps = check_keras_overrides(model, feature, num_classes, timesteps, batch_size)

    logger.info('Building model')
    try:
        hypermodel = model.MyHyperModel(feature=feature,
                                        num_classes=num_classes,
                                        timesteps=timesteps,
                                        batch_size=batch_size)
        built_model = hypermodel.build_model(kt.HyperParameters())
    except Exception as e:
        logger.exception(f'Error: build_model() in {model_base} failed: {e}.')
        raise SystemExit(1)

    logger.info(f'Summary of {model_base}:')
    kb.clear_session()
    logger.info('')
    built_model.summary(print_fn=logger.info)
    logger.info('')
    logger.info(f'feature       {hypermodel.feature}')
    logger.info(f'num_classes   {hypermodel.num_classes}')
    logger.info(f'timesteps     {hypermodel.timesteps}')
    logger.info(f'batch_size    {hypermodel.batch_size}')
    logger.info(f'flatten       {hypermodel.flatten}')
    logger.info(f'add1ch        {hypermodel.add1ch}')
    logger.info(f'truth_mutex   {hypermodel.truth_mutex}')
    logger.info(f'lossf         {hypermodel.lossf}')
    logger.info(f'input_shape   {hypermodel.input_shape}')
    logger.info(f'optimizer     {built_model.optimizer.get_config()}')
    logger.info('')

    logger.info(f'Loading weights from {weights_name}')
    built_model.load_weights(weights_name)

    files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.h5']

    # Convert WAV to feature data
    wav_files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.wav']
    for file in wav_files:
        audio = read_audio(file)
        data = get_feature_from_audio(audio=audio, feature=feature)

        output_name = join(output_dir, basename(splitext(file)[0]))
        if exists(output_name + '.h5'):
            # If an H5 file of the same name as the WAV file already exists, then append '_wav'
            # to the output file name.
            output_name += '_wav'
        output_name += '.h5'
        files.append(output_name)
        # Save the newly created feature
        with h5py.File(output_name, 'a') as f:
            if 'feature' in f:
                del f['feature']
            f.create_dataset(name='feature', data=data, dtype=np.single)

    files = sorted(files)
    logger.info(f'Found {len(files)} files from {input_name}')

    if reset:
        # reset mode cycles through each file one at a time
        frames_per_batch = get_frames_per_batch(hypermodel.batch_size, hypermodel.timesteps)
        for file in files:
            # Read in H5
            with h5py.File(file, 'r') as f:
                data = np.array(f['feature'])

            # Pad with zeros in order to create an entire batches of data
            frames = data.shape[0]
            padding = frames_per_batch - data.shape[0] % frames_per_batch
            data = np.pad(array=data,
                          pad_width=((0, padding), (0, 0), (0, 0)),
                          mode='constant',
                          constant_values=0)
            data, _, _, _, _, _ = reshape_inputs(feature=data,
                                                 batch_size=hypermodel.batch_size,
                                                 timesteps=hypermodel.timesteps,
                                                 flatten=hypermodel.flatten,
                                                 add1ch=hypermodel.add1ch)
            predict = built_model.predict(data, verbose=1)
            predict, _, _ = reshape_outputs(predict=predict, timesteps=hypermodel.timesteps)
            predict = predict[:frames, :]

            output_name = join(output_dir, basename(file))
            with h5py.File(output_name, 'a') as f:
                if 'predict' in f:
                    del f['predict']
                f.create_dataset(name='predict', data=predict, dtype=np.single)
    else:
        # Run all data at once using a data generator
        data = SequenceFromH5(files=files,
                              feature=feature,
                              num_classes=num_classes,
                              batch_size=hypermodel.batch_size,
                              timesteps=hypermodel.timesteps,
                              flatten=hypermodel.flatten,
                              add1ch=hypermodel.add1ch,
                              truth_mutex=hypermodel.truth_mutex)

        predict = built_model.predict(data, verbose=1)
        predict, _, _ = reshape_outputs(predict=predict, timesteps=hypermodel.timesteps)

        for idx, file in enumerate(files):
            output_name = join(output_dir, basename(file))
            with h5py.File(output_name, 'a') as f:
                if 'predict' in f:
                    del f['predict']
                f.create_dataset('predict', data=predict[data.file_indices[idx]], dtype=np.single)

    logger.info(f'Saved results to {output_dir}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()
