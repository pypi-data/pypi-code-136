"""sonusai keras_train

usage: keras_train [-hv] (-m MODEL) (-d MIXDB) [--tloc TLOC] [-l VMIXDB] [--vloc VLOC]
                    [-e EPOCHS] [-b BATCH] [-t TSTEPS] [-p ESP] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -m MODEL, --model MODEL         Model Python file with build and/or hypermodel functions.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    --tloc TLOC                     Data location.
    -l VMIXDB, --vmixdb VMIXDB      Validation split (0 - 1) or validation mixdb. [default: 0.2].
    --vloc VLOC                     Validation data location.
    -e EPOCHS, --epochs EPOCHS      Number of epochs to use in training. [default: 8].
    -b BATCH, --batch BATCH         Batch size.
    -t TSTEPS, --tsteps TSTEPS      Timesteps.
    -p ESP, --patience ESP          Early stopping patience.
    -o OUTPUT, --output OUTPUT      Output directory.

Use Keras to train a model defined by a Python definition file and SonusAI genft data.

Inputs:
    MIXDB   A SonusAI mixture database JSON file.
    TLOC    Optional training data directory containing genft data.
    VMIXDB  A validation data split (0 - 1) or a SonusAI mixture database JSON file to use for validation data.
    VLOC    Optional validation data directory containing genft data; only used when VMIXDB is a JSON mixdb.

Validation is created from MIXDB data using a split of VMIXDB if VMIXDB is a number between 0 and 1, or from VMIXDB
if VMIXDB is a SonusAI mixture database JSON file.

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
    t_name = args['--mixdb']
    t_loc = args['--tloc']
    v_name = args['--vmixdb']
    v_loc = args['--vloc']
    epochs = int(args['--epochs'])
    batch_size = args['--batch']
    timesteps = args['--tsteps']
    esp = args['--patience']
    output_dir = args['--output']

    from os import makedirs
    from os import walk
    from os.path import basename
    from os.path import join
    from os.path import splitext

    import h5py
    import keras2onnx
    import keras_tuner as kt
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras import backend as kb
    from tensorflow.keras.callbacks import EarlyStopping

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.data_generator import KerasFromH5
    from sonusai.mixture import get_class_count_from_mixids
    from sonusai.mixture import load_mixdb
    from sonusai.mixture import new_mixdb_from_mixids
    from sonusai.utils import check_keras_overrides
    from sonusai.utils import create_ts_name
    from sonusai.utils import import_keras_model
    from sonusai.utils import stratified_shuffle_split_mixid

    v_mixdb = None
    v_split = None
    try:
        v_split = float(v_name)
        if v_split < 0 or v_split > 1:
            logger.exception('--vmixdb must be between 0 and 1')
            raise SystemExit(1)
    except ValueError:
        v_mixdb = load_mixdb(v_name)
        if v_loc is None:
            v_loc = splitext(v_name)[0]

    if t_loc is None:
        t_loc = splitext(t_name)[0]

    model_base = basename(model_name)
    model_root = splitext(model_base)[0]

    if batch_size is not None:
        batch_size = int(batch_size)

    if timesteps is not None:
        timesteps = int(timesteps)

    if output_dir is None:
        output_dir = create_ts_name(model_root)

    makedirs(output_dir, exist_ok=True)
    base_name = join(output_dir, model_root)

    # Setup logging file
    create_file_handler(join(output_dir, 'keras_train.log'))
    update_console_handler(verbose)
    initial_log_messages('keras_train')

    logger.info(f'TF ver: {tf.__version__}')
    logger.info(f'Keras ver: {tf.keras.__version__}')
    logger.info(f'Keras2onnx ver: {keras2onnx.__version__}')
    logger.info('')

    t_mixdb = load_mixdb(t_name)
    t_num_mixtures = len(t_mixdb.mixtures)
    logger.info(f'Found {t_num_mixtures} mixtures with {t_mixdb.num_classes} classes from {t_name}')

    # Import model definition file
    logger.info(f'Importing {model_base}')
    model = import_keras_model(model_name)

    # Check overrides
    timesteps = check_keras_overrides(model, t_mixdb.feature, t_mixdb.num_classes, timesteps, batch_size)

    logger.info('Building model')
    try:
        hypermodel = model.MyHyperModel(feature=t_mixdb.feature,
                                        num_classes=t_mixdb.num_classes,
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

    stratify = False
    if v_mixdb is not None:
        # Validation data from v_mixdb
        logger.info(f'Validation data from {v_name}.')
        v_mixid = range(len(v_mixdb.mixtures))
        if stratify:
            logger.info(f'Stratifying training data.')
            t_mixid, _, _, _ = stratified_shuffle_split_mixid(t_mixdb, vsplit=0)
        else:
            t_mixid = range(t_num_mixtures)
    else:
        # Validation data from v_split
        logger.info(f'Validation data from {t_name} using split of {v_split}.')
        v_mixdb = t_mixdb
        v_loc = t_loc
        if stratify:
            logger.info(f'Stratifying training and validation data.')
            t_mixid, v_mixid, _, _ = stratified_shuffle_split_mixid(t_mixdb, vsplit=v_split)
        else:
            t_split_mixtures = int(np.ceil((1 - v_split) * t_num_mixtures))
            t_mixid = range(t_split_mixtures)
            v_mixid = range(t_split_mixtures, t_num_mixtures)

    logger.info(f'{len(t_mixid)} training mixtures and {len(v_mixid)} validation mixtures.')

    # Use SonusAI DataGenerator to create validation feature/truth on the fly
    v_datagen = KerasFromH5(mixdb=v_mixdb,
                            mixids=v_mixid,
                            location=v_loc,
                            batch_size=batch_size,
                            timesteps=timesteps,
                            flatten=hypermodel.flatten,
                            add1ch=hypermodel.add1ch,
                            shuffle=False)

    # Prepare class weighting
    class_count = np.ceil(np.array(get_class_count_from_mixids(t_mixdb, t_mixid)) / t_mixdb.feature_step_samples)
    if t_mixdb.truth_mutex:
        other_weight = 16.0
        logger.info(f'Detected single-label mode (truth_mutex); setting other weight to {other_weight}.')
        class_count[-1] = class_count[-1] / other_weight

    # Use SonusAI DataGenerator to create training feature/truth on the fly
    t_datagen = KerasFromH5(mixdb=t_mixdb,
                            mixids=t_mixid,
                            location=t_loc,
                            batch_size=batch_size,
                            timesteps=timesteps,
                            flatten=hypermodel.flatten,
                            add1ch=hypermodel.add1ch,
                            shuffle=True)

    # TODO: If hypermodel.es exists, then use it; otherwise use default here
    if esp is None:
        es = EarlyStopping(monitor='val_loss',
                           mode='min',
                           verbose=1,
                           patience=8)
    else:
        es = EarlyStopping(monitor='val_loss',
                           mode='min',
                           verbose=1,
                           patience=esp)

    ckpt_callback = tf.keras.callbacks.ModelCheckpoint(filepath=base_name + '-ckpt-weights.h5',
                                                       save_weights_only=True,
                                                       monitor='val_loss',
                                                       mode='min',
                                                       save_best_only=True)

    logger.info('')
    logger.info(f'Training with no class weighting and early stopping patience = {es.patience}')
    logger.info('')

    history = built_model.fit(t_datagen,
                              batch_size=batch_size,
                              epochs=epochs,
                              validation_data=v_datagen,
                              shuffle=False,
                              callbacks=[es, ckpt_callback])

    # Save history into numpy file
    history_name = base_name + '-history'
    np.save(history_name, history.history)
    # Note: Reload with history=np.load(history_name, allow_pickle='TRUE').item()
    logger.info(f'Saved training history to numpy file {history_name}.npy')

    # Find checkpoint file and load weights for prediction and model save
    checkpoint_name = None
    for path, dirs, files in walk(output_dir):
        for f in files:
            if "ckpt" in f:
                checkpoint_name = f

    if checkpoint_name is not None:
        logger.info('Using best checkpoint for prediction and model exports')
        built_model.load_weights(join(output_dir, checkpoint_name))
    else:
        logger.info('Using last epoch for prediction and model exports')

    # save for later model export(s)
    weight_name = base_name + '.h5'
    built_model.save(weight_name)
    with h5py.File(weight_name, 'a') as f:
        f.attrs['sonusai_feature'] = hypermodel.feature
        f.attrs['sonusai_num_classes'] = str(hypermodel.num_classes)

    logger.info(f'Saved trained model to {weight_name}')

    # Compute prediction metrics on validation data using the best checkpoint
    # t_mixid, v_mixid, or entire dataset mixdb
    v_mixdb = new_mixdb_from_mixids(t_mixdb, v_mixid)
    v_predict = built_model.predict(x=v_datagen, batch_size=batch_size, verbose=1)
    v_predict_name = base_name + '-valpredict.h5'
    with h5py.File(v_predict_name, 'w') as f:
        f.create_dataset('predict', data=v_predict)
        f.attrs['mixdb'] = v_mixdb.to_json()

    logger.info(f'Wrote prediction and truth to file {v_predict_name}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()
