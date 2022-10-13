"""sonusai predict

usage: predict [-hvr] (-m MODEL) (-d INPUT) [-o OUTPUT]

options:
    -h, --help
    -v, --verbose               Be verbose.
    -m MODEL, --model MODEL     Trained ONNX model file.
    -d INPUT, --input INPUT     Input WAV or genft directory.
    -o OUTPUT, --output OUTPUT  Output directory.
    -r, --reset                 Reset model between each file.

Run prediction on a trained ONNX model using SonusAI genft data.

Inputs:
    MODEL       A SonusAI trained ONNX model file.
    INPUT       A WAV file or a directory containing genft data.

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5
                        dataset:    predict
                    predict.log

"""
from sonusai import logger


def main():
    import time
    from os import makedirs
    from os.path import basename
    from os.path import exists
    from os.path import join
    from os.path import splitext

    import h5py
    import numpy as np
    from docopt import docopt
    from pyaaware import Predict

    import sonusai
    from sonusai import SonusAIError
    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import logger
    from sonusai import update_console_handler
    from sonusai.mixture import get_feature_from_audio
    from sonusai.mixture import read_audio
    from sonusai.utils import create_ts_name
    from sonusai.utils import seconds_to_hms
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    model_name = args['--model']
    input_name = args['--input']
    output_dir = args['--output']

    model_tail = basename(model_name)
    model_root = splitext(model_tail)[0]

    start_time = time.monotonic()

    if output_dir is None:
        output_dir = create_ts_name(model_root)

    makedirs(output_dir, exist_ok=True)
    base_name = join(output_dir, model_root)

    # Setup logging file
    create_file_handler(join(output_dir, 'predict.log'))
    update_console_handler(verbose)
    initial_log_messages('predict')

    logger.info('')
    logger.info(f'Model:  {model_name}')
    logger.info(f'Input:  {input_name}')
    logger.info(f'Output: {output_dir}')
    logger.info('')

    model = Predict(model_name)
    logger.debug(f'Model feature name {model.feature}')
    logger.debug(f'Model input shape  {model.input_shape}')
    logger.debug(f'Model output shape {model.output_shape}')

    if not exists(input_name):
        raise SonusAIError(f'{input_name} does not exist')

    ext = splitext(input_name)[1]

    if ext == '.wav':
        audio = read_audio(input_name)
        feature = get_feature_from_audio(audio=audio, feature=model.feature)
    elif ext == '.h5':
        with h5py.File(input_name, 'r') as f:
            feature = np.array(f['/feature'])
    else:
        raise SonusAIError(f'Unknown file type for {input_name}')

    logger.debug(f'Input shape        {feature.shape}')

    predict = model.execute(feature)

    # if expect_name:
    #     with h5py.File(expect_name, 'r') as f:
    #         expected = np.array(f['/predict'])
    #         logger.debug(f'Expect shape {expected.shape}')
    #         if expected.shape != predict.shape:
    #             raise SonusAIError('Expect shape does not match input shape')
    #
    #         max_error = np.amax(np.abs(predict - expected))
    #         logger.info(f'Maximum error = {max_error}')

    if output_dir:
        with h5py.File(output_dir, 'w') as f:
            f.create_dataset(name='predict', data=predict)
            logger.info(f'Wrote {output_dir}')

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
