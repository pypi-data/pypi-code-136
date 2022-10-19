"""sonusai keras_predict

usage: keras_predict [-hvr] (-m MODEL) (-w KMODEL) (-d INPUT) [-b BATCH] [-t TSTEPS] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -m MODEL, --model MODEL         Python model file.
    -w KMODEL, --weights KMODEL     Keras model weights file.
    -d INPUT, --input INPUT         Input data.
    -b BATCH, --batch BATCH         Batch size.
    -t TSTEPS, --tsteps TSTEPS      Timesteps.
    -o OUTPUT, --output OUTPUT      Output directory.
    -r, --reset                     Reset model between each file.

Run prediction on a trained Keras model defined by a SonusAI Keras Python model file using SonusAI genft data
and/or WAV data.

Inputs:
    MODEL       A SonusAI Python model file with build and/or hypermodel functions.
    KMODEL      A Keras model weights file (or model file with weights).
    INPUT       The input data can be a file, directory, or glob of genft H5 files and/or WAV files.

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5
                        dataset:    predict
                    keras_predict.log

Results are written into subdirectory kpredict-<TIMESTAMP> unless OUTPUT is specified.

"""
from sonusai import logger


def main():
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    model_name = args['--model']
    weights_name = args['--weights']
    input_name = args['--input']
    batch_size = args['--batch']
    timesteps = args['--tsteps']
    output_dir = args['--output']
    reset = args['--reset']

    from os import makedirs
    from os.path import basename
    from os.path import isdir
    from os.path import join
    from os.path import splitext

    import h5py
    import keras_tuner as kt
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras import backend as kb

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.data_generator import SequenceFromH5
    from sonusai.data_generator import get_frames_per_batch
    from sonusai.mixture import get_feature_from_audio
    from sonusai.mixture import read_audio
    from sonusai.utils import braced_glob
    from sonusai.utils import check_keras_overrides
    from sonusai.utils import create_ts_name
    from sonusai.utils import import_keras_model
    from sonusai.utils import reshape_inputs
    from sonusai.utils import reshape_outputs

    model_base = basename(model_name)

    if batch_size is not None:
        batch_size = int(batch_size)

    if timesteps is not None:
        timesteps = int(timesteps)

    if output_dir is None:
        output_dir = create_ts_name('kpredict')

    makedirs(output_dir, exist_ok=True)

    # Setup logging file
    create_file_handler(join(output_dir, 'keras_predict.log'))
    update_console_handler(verbose)
    initial_log_messages('keras_predict')

    logger.info(f'tensorflow    {tf.__version__}')
    logger.info(f'keras         {tf.keras.__version__}')
    logger.info('')

    # Import model definition file
    logger.info(f'Importing {model_base}')
    model = import_keras_model(model_name)
    feature = None
    num_classes = None
    with h5py.File(weights_name, 'r') as f:
        if 'sonusai_feature' in f.attrs:
            feature = f.attrs['sonusai_feature']
        else:
            logger.warn(f'Could not find SonusAI feature in weights file; using hypermodel default.')
        if 'sonusai_num_classes' in f.attrs:
            num_classes = int(f.attrs['sonusai_num_classes'])
        else:
            logger.warn(f'Could not find SonusAI num_classes in weights file; using hypermodel default.')

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

    frames_per_batch = get_frames_per_batch(hypermodel.batch_size, hypermodel.timesteps)

    kb.clear_session()
    logger.info('')
    built_model.summary(print_fn=logger.info)
    logger.info('')
    logger.info(f'feature       {hypermodel.feature}')
    logger.info(f'num_classes   {hypermodel.num_classes}')
    logger.info(f'batch_size    {hypermodel.batch_size}')
    logger.info(f'timesteps     {hypermodel.timesteps}')
    logger.info(f'flatten       {hypermodel.flatten}')
    logger.info(f'add1ch        {hypermodel.add1ch}')
    logger.info(f'truth_mutex   {hypermodel.truth_mutex}')
    logger.info(f'lossf         {hypermodel.lossf}')
    logger.info(f'input_shape   {hypermodel.input_shape}')
    logger.info(f'optimizer     {built_model.optimizer.get_config()}')
    logger.info('')

    logger.info(f'Loading weights from {weights_name}')
    built_model.load_weights(weights_name)

    if isdir(input_name):
        input_name = join(input_name, '*.{h5,wav}')

    files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.h5']

    # Convert WAV to feature data
    wav_files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.wav']
    for file in wav_files:
        audio = read_audio(file)
        data = get_feature_from_audio(audio=audio, feature=feature)

        output_base = basename(splitext(file)[0])
        output_name = join(output_dir, output_base)
        if output_base + '.h5' in [basename(x) for x in files]:
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
        for file in files:
            # Read in H5
            with h5py.File(file, 'r') as f:
                data = np.array(f['feature'])

            # Pad with zeros in order to create an entire batch of data
            frames = data.shape[0]
            padding = frames_per_batch - frames % frames_per_batch
            data = np.pad(array=data,
                          pad_width=((0, padding), (0, 0), (0, 0)),
                          mode='constant',
                          constant_values=0)
            data, _, _, _, _, _ = reshape_inputs(feature=data,
                                                 batch_size=hypermodel.batch_size,
                                                 timesteps=hypermodel.timesteps,
                                                 flatten=hypermodel.flatten,
                                                 add1ch=hypermodel.add1ch)

            predict = built_model.predict(data, batch_size=hypermodel.batch_size, verbose=1)
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

        predict = built_model.predict(data, batch_size=hypermodel.batch_size, verbose=1)
        predict, _, _ = reshape_outputs(predict=predict, timesteps=hypermodel.timesteps)

        # Write data to separate files
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
