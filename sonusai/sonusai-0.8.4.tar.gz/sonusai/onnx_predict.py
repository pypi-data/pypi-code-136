"""sonusai predict

usage: predict [-hvr] (-m MODEL) (-d INPUT) [-o OUTPUT]

options:
    -h, --help
    -v, --verbose               Be verbose.
    -m MODEL, --model MODEL     Trained ONNX model file.
    -d INPUT, --input INPUT     Input data.
    -o OUTPUT, --output OUTPUT  Output directory.
    -r, --reset                 Reset model between each file.

Run prediction on a trained ONNX model using SonusAI genft data and/or WAV data.

Inputs:
    MODEL       A SonusAI trained ONNX model file.
    INPUT       The input data can be a file, directory, or glob of genft H5 files and/or WAV files.

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5
                        dataset:    predict
                    predict.log

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
    output_dir = args['--output']
    reset = args['--reset']

    from os import makedirs
    from os.path import basename
    from os.path import isdir
    from os.path import join
    from os.path import splitext

    import h5py
    import numpy as np
    from pyaaware import Predict

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.data_generator import get_frames_per_batch
    from sonusai.mixture import get_feature_from_audio
    from sonusai.mixture import read_audio
    from sonusai.utils import braced_glob
    from sonusai.utils import create_ts_name
    from sonusai.utils import reshape_inputs
    from sonusai.utils import reshape_outputs

    if output_dir is None:
        output_dir = create_ts_name('opredict')

    makedirs(output_dir, exist_ok=True)

    # Setup logging file
    create_file_handler(join(output_dir, 'onnx_predict.log'))
    update_console_handler(verbose)
    initial_log_messages('onnx_predict')

    model = Predict(model_name)
    batch_size = model.input_shape[0]
    if model.timestep:
        timesteps = model.input_shape[1]
    else:
        timesteps = 0
    num_classes = model.output_shape[-1]

    frames_per_batch = get_frames_per_batch(batch_size, timesteps)

    logger.info('')
    logger.info(f'feature       {model.feature}')
    logger.info(f'num_classes   {num_classes}')
    logger.info(f'batch_size    {batch_size}')
    logger.info(f'timesteps     {timesteps}')
    logger.info(f'flatten       {model.flattened}')
    logger.info(f'add1ch        {model.channel}')
    logger.info(f'truth_mutex   {model.mutex}')
    logger.info(f'input_shape   {model.input_shape}')
    logger.info(f'output_shape  {model.output_shape}')
    logger.info('')

    if isdir(input_name):
        input_name = join(input_name, '*.{h5,wav}')

    files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.h5']

    # Convert WAV to feature data
    wav_files = [x for x in braced_glob(input_name) if splitext(x)[1] == '.wav']
    for file in wav_files:
        audio = read_audio(file)
        data = get_feature_from_audio(audio=audio, feature=model.feature)

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
            padding = frames_per_batch - data.shape[0] % frames_per_batch
            data = np.pad(array=data,
                          pad_width=((0, padding), (0, 0), (0, 0)),
                          mode='constant',
                          constant_values=0)
            data, _, _, _, _, _ = reshape_inputs(feature=data,
                                                 batch_size=batch_size,
                                                 timesteps=timesteps,
                                                 flatten=model.flattened,
                                                 add1ch=model.channel)

            # Create new model for each file; simulates reset
            model = Predict(model_name)
            predict = model.execute(data)
            predict, _, _ = reshape_outputs(predict=predict, timesteps=timesteps)
            predict = predict[:frames, :]

            output_name = join(output_dir, basename(file))
            with h5py.File(output_name, 'a') as f:
                if 'predict' in f:
                    del f['predict']
                f.create_dataset(name='predict', data=predict, dtype=np.single)
    else:
        # Read in H5s
        data = []
        file_indices = []
        total_frames = 0
        for file in files:
            with h5py.File(file, 'r') as f:
                current_data = np.array(f['feature'])
                current_frames = current_data.shape[0]
                data.append(current_data)
                file_indices.append(slice(total_frames, total_frames + current_frames))
                total_frames += current_frames
        data = np.vstack([data[i] for i in range(len(data))])

        # Pad with zeros in order to create an entire batch of data
        frames = data.shape[0]
        padding = frames_per_batch - frames % frames_per_batch
        data = np.pad(array=data,
                      pad_width=((0, padding), (0, 0), (0, 0)),
                      mode='constant',
                      constant_values=0)

        data, _, _, _, _, _ = reshape_inputs(feature=data,
                                             batch_size=batch_size,
                                             timesteps=timesteps,
                                             flatten=model.flattened,
                                             add1ch=model.channel)

        predict = model.execute(data)
        predict, _, _ = reshape_outputs(predict=predict, timesteps=timesteps)
        predict = predict[:frames, :]

        # Write data to separate files
        for idx, file in enumerate(files):
            output_name = join(output_dir, basename(file))
            with h5py.File(output_name, 'a') as f:
                if 'predict' in f:
                    del f['predict']
                f.create_dataset('predict', data=predict[file_indices[idx]], dtype=np.single)

    logger.info(f'Saved results to {output_dir}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
