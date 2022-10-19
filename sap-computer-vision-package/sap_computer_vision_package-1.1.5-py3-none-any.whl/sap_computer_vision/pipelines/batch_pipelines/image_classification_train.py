import pathlib
import json
import os
import zipfile
from functools import lru_cache
import logging

from fvcore.common.config import BASE_KEY
from metaflow import FlowSpec, step, argo, Parameter, JSONType

from detectron2.config import CfgNode

import sap_computer_vision.datasets.utils as utils
from sap_computer_vision.datasets import image_folder as imgf
from sap_computer_vision import get_cfg, get_config_file, setup_loggers
from sap_computer_vision.evaluators import ImageClassificationEvaluator
from sap_computer_vision.engine import ImageClassificationTrainer

MODEL_OUTPUT_DIR = str(pathlib.Path('/tmp/model'))
DATA_INPUT_DIR = pathlib.Path('/tmp/datain')

# TODO: Data loading process not finished and try to match what we implemented for object detection


class Trainer(ImageClassificationTrainer):
    @classmethod
    def build_evaluator(cls, cfg, dataset_name):
        if cfg.TEST.EVAL_PERIOD <= 0:
            raise NotImplementedError
        else:
            return ImageClassificationEvaluator(cfg)  # pylint: disable=E1124,E1125


class ImageClassificationTrain(FlowSpec):
    """Pipeline to train a model for image classification.
    """
    model_name = Parameter("model_name",
                           help="Name of the Model configuration file.",
                           default="ImageClassifier/FPN-Resnet50-no-pooling")

    train_input = Parameter("train",
                         help=f"Name of the file within {DATA_INPUT_DIR} containing filenames of the train dataset.",
                         default='train.txt')

    validation_input = Parameter("validation",
                       help=f"Name of the file within {DATA_INPUT_DIR} containing filenames of the validation dataset.",
                       default="val.txt")

    test_input = Parameter("test",
                        help=f"Name of the file within {DATA_INPUT_DIR} containing filenames of the test dataset.",
                        default="val.txt")

    class_names = Parameter("class_names",
                            help="JSON encoded list of class names. If it is empty or not a valid JSON, " + \
                                 "classes will be extracted from the train/val/test datasets.",
                            default="")

    batch_size = Parameter("batch_size",
                           help="Number of images per batch.",
                           default=40)

    lr_decay = Parameter("learning_rate_decay",
                         help="Whether learning rate should be decreased over the training.",
                         default=True)

    intermediate_layers = Parameter("projection_layers",
                         help="Size of layers between backbone and final output layer. If [] , no intermediate layer is used.",
                         type=JSONType,
                         default=json.dumps([]))

    n_steps = Parameter("maximum_training_steps",
                        help="Maximum number of training steps. Actual training steps could be less if `early_stopping` is enabled.",
                        default=3000)

    eval_freq = Parameter("evaluation_frequency",
                          help="Frequency of evaluation. If > 1 it is treated as every `evaluation_frequency` steps. " + \
                               "If < 1 an evaluation in done every `evaluation_frequency` * `maximum_training_steps` steps",
                          default=0.1)

    base_lr = Parameter("base_learning_rate",
                        help="Base learning rate.",
                        default=0.00025)

    imgtypes = Parameter("image_types",
                         help="JSON encoded list of expected file extensions for images",
                         type=JSONType,
                         default=json.dumps([".jpg", ".jpeg", ".png"]))

    additional_augmentations = Parameter("additional_augmentations",
                                         help="Whether as additional data augmentations like cropping, random saturation, " + \
                                              "random lighting, random brightness and random contrast should be done.",
                                         default=True)

    log_metrics_aif = Parameter("aicore_tracking",
                                help="Whether the evaluator should log the metrics on AI Core, so you can track your pipeline execution on AI Core",
                                type=bool,
                                default=False)

    seed = Parameter("seed",
                     help="Random seed.",
                     default=1337)

    @argo(output_artifacts=[{'name': 'trainedmodel',
                             'globalName': 'trainedmodel',
                             'path': str(MODEL_OUTPUT_DIR),
                             'archive': {'none': {}}}],
          input_artifacts=[{'name': 'datain',
                            'path': str(DATA_INPUT_DIR)}],
          labels={"ai.sap.com/resourcePlan": "train.l"},
          shared_memory=1000)
    @step
    def start(self):
        logger = setup_loggers(str(MODEL_OUTPUT_DIR), color=False, additional_loggers=[__name__])
        self.eval_frequency = float(self.eval_freq)
        class_names = None if self.class_names == "" else json.loads(self.class_names)
        img_extensions = utils.check_extensions(self.imgtypes)
        self.datasets, self.class_names_used = self.prepare_input_data(DATA_INPUT_DIR,
                                                                       train=self.train_input,
                                                                       validation=self.validation_input,
                                                                       test=self.test_input,
                                                                       class_names=class_names,
                                                                       img_extensions=img_extensions,
                                                                       seed=self.seed)
        cfg = self.get_train_cfg(self.datasets, self.class_names_used )

        modul_output_path = pathlib.Path(MODEL_OUTPUT_DIR)
        modul_output_path.mkdir(parents=True, exist_ok=True)
        with (modul_output_path / 'used_config.yaml').open('w') as stream:
            stream.write(cfg.dump())

        trainer = Trainer(cfg)
        trainer.resume_or_load(resume=False)
        trainer.train()

        test_name = f'test'

        if test_name in self.datasets:
            cfg.defrost()
            cfg.DATASETS.TEST = (test_name,)

            results_test = trainer.test(cfg, trainer.model) #  # pylint: disable=E1101
            with open(cfg.OUTPUT_DIR + '/metrics_test.json', 'w') as stream:
                json.dump(results_test, stream, indent=2)

            if self.log_metrics_aif:
                try:
                    from ai_core_sdk.tracking import Tracking
                except ImportError:
                    logger.warn("AI Core Tracking Module not found!")
                else:
                    from sap_computer_vision.engine.trainers import AIFLogging

                    tracking_module = Tracking()
                    formatted_metrics = AIFLogging.format_metrics(results_test, step=trainer.iter, labels=[{'name': 'data_split', 'value': 'test'}])
                    tracking_module.log_metrics(metrics=formatted_metrics)

        self.next(self.end)

    @step
    def end(self):
        pass

    @staticmethod
    def prepare_input_data(base_dir, class_names=None, img_extensions=None, seed=None, **dataset_inputs):
        f'''This function interprets the \'train\', \'test\', \'validation\' parameters.

        To register a dataset in detectron a lightweight version (list of dicts) of the dataset has to be created.
        The folder in which the images are located is used as the label for each image.
        So there must be a subfolder in the input artifact for each class.

        For the \'train\', \'test\', \'validation\' parameters in this pipeline different options are supported.
        The input data is provided as an input artifact and is copy to {DATA_INPUT_DIR}. The parameters for the
        different dataset can be either a subfolder with the input directory, a txt-file containing the filenames
        or a float between zero and 1.

        Examples
        ---------
            1.)
                Structure of the input artifact:
                input_artifact/
                    train/
                        class_1/
                            img1.jpg
                            img2.jpg
                        class_2/
                            ...
                        ...
                    val/
                        class_1/
                            img231.jpg
                            img2123.jpg
                        class_2/
                            ...
                        ...
                    test/
                        class_1/
                            img3213.jpg
                            img32231.jpg
                        class_2/
                            ...
                        ...

                Parameter values:
                \'train\'='train'
                \'validation\'='val'
                \'test\'='test'

                In this example the values of the parameters are relative paths to subfolders
                located in the input artifact.
                The files in the subfolders are used for the corresponding dataset.
            2.)
                Structure of the input artifact:
                input_artifact/
                    class_1/
                        img1.jpg
                        img2.jpg
                    class_2/
                        ...
                    ...
                    splits/
                        train.txt
                        val.txt
                        test.txt

                Parameter values:
                \'train\'='splits/train.txt'
                \'validation\'='splits/val.txt'
                \'test\'='splits/test.txt'
                In this example the values of the parameters are paths to txt files within the in the input artifact.
                The txt-files are expected to contain the file names (1 file name per line with or with file ending)
                for the datasets.
            3.)
                Structure of the input artifact:
                class_1/
                    img1.jpg
                    img2.jpg
                class_2/
                    ...
                ...
                Parameter values:
                \'train\'=0.8
                \'validation\'=0.2
                \'test\'=''
                In this example the values of the parameters are float values and '' for the test parameter.
                The numbers indicate which part of the files in the images/annotation folders should be used
                for the dataset. In the result folder of the pipeline a txt-file for each split will be placed.
                \'validation\' and \'test\' can be in empty string in all cases. If they are set
                to an empty string no evaluation/test is performed during the training.
            '''
        if img_extensions is None:
            img_extensions = ['*.jpg', '*.jpeg']

        base_dir = pathlib.Path(base_dir)

        logger = logging.getLogger(__name__)
        logger.info(f"Preparing datsets:")

        @lru_cache(None)
        def _prepare_input_data(input):
            input_data = None
            if input != '' and input is not None:
                input_data = base_dir / str(input)
                if input_data.exists() and input_data.is_dir():
                    pass
                elif input_data.exists() and input_data.is_file():
                    if input_data.suffix == '.zip':
                        with zipfile.ZipFile(input_data, 'r') as zip_ref:
                            input_data_extracted = input_data.with_suffix('')
                            zip_ref.extractall(input_data_extracted)
                        os.remove(input_data)
                        input_data = input_data_extracted
                else:
                    try:
                        input_data = float(input)
                    except ValueError:
                        input_data = None
            return input_data

        for name, value in dataset_inputs.items():
            prepared = _prepare_input_data(value)
            dataset_inputs[name] = prepared
            logger.info(f"Parameter '{name}'={value} -> {prepared}")

        primary_parameter = next(iter(dataset_inputs.values()))
        if isinstance(primary_parameter, pathlib.Path):
            datasets = {}
            for n, input_ in dataset_inputs.items():
                if isinstance(input_, pathlib.Path):
                    datasets[n], class_names = imgf.register(n,
                                                             class_names=class_names,
                                                             extensions=img_extensions,
                                                             base_dir=(base_dir if input_.is_file() else input_),
                                                             filenames=(input_ if input_.is_file() else None))
        elif isinstance(primary_parameter, float):
            splits = {n: v for n, v in dataset_inputs.items() if isinstance(v, float)}
            datasets, class_names = imgf.split_and_register('',
                                                            base_dir=base_dir,
                                                            splits=splits,
                                                            extensions=img_extensions,
                                                            rnd_gen=seed)
            for n, file_ids in datasets.items():
                with (pathlib.Path(MODEL_OUTPUT_DIR) / f'{n}.txt').open('w') as stream:
                    stream.write('\n'.join([str(f) for f in file_ids]))
        else:
            raise ValueError(f'Invalid input for train data! Input artifact content: {os.listdir(base_dir)}')
        logger.info(f"Successfully registed datasets:")
        for n, v in datasets.items():
            logger.info(f"{n} with {len(v)} examples")
        return datasets, class_names

    def get_train_cfg(self, datasets, class_names):
        cfg = get_cfg()
        cfg.merge_from_file(get_config_file('Base-EarlyStopping'))
        cfg.merge_from_file(get_config_file('Base-Evaluation'))
        cfg.merge_from_file(get_config_file(self.model_name))
        cfg.SEED = int(self.seed)
        cfg.OUTPUT_DIR = MODEL_OUTPUT_DIR
        cfg.DATASETS.TRAIN = ('train',)
        if 'validation' in datasets.keys():
            cfg.DATASETS.TEST = (f'validation',)
            if self.eval_frequency > 1:
                cfg.TEST.EVAL_PERIOD = int(self.eval_frequency)
            else:
                cfg.TEST.EVAL_PERIOD = int(cfg.SOLVER.MAX_ITER * float(self.eval_frequency))
        else:
            cfg.DATASETS.TEST = None
            cfg.TEST.EVAL_PERIOD = -1
        cfg.SOLVER.BASE_LR = float(self.base_lr)
        cfg.SOLVER.MAX_ITER = int(self.n_steps)
        cfg.SOLVER.IMS_PER_BATCH = int(self.batch_size)
        cfg.SOLVER.WARMUP_ITERS = max(int(0.01 * cfg.SOLVER.MAX_ITER), 0)
        if self.lr_decay:
            cfg.SOLVER.STEPS = [cfg.SOLVER.MAX_ITER * p for p in (0.5, 0.75, 0.9)]
        else:
            cfg.SOLVER.STEPS = []

        cfg.set_new_allowed(True)
        cfg.TRAINING_INFO = CfgNode()
        cfg.TRAINING_INFO.THING_CLASSES = class_names
        cfg.TRAINING_INFO.TASK = 'IMAGE_CLASSIFICATION'

        cfg.MODEL.FEATURE_EXTRACTION.INTERMEDIATE_SIZE = self.intermediate_layers
        cfg.MODEL.IMAGE_CLASSIFIER.NUM_CLASSES = len(class_names)
        cfg.EVAL.LOG_METRICS = bool(self.log_metrics_aif)
        for aug in ['RANDOM_LIGHTING', 'RANDOM_BRIGHTNESS', 'RANDOM_SATURATION', 'RANDOM_CONTRAST', 'RANDOM_ROTATION', 'CROP']:
            if cfg.INPUT.get(aug, None) is not None:
                cfg.INPUT[aug].ENABLED = self.additional_augmentations
        cfg.freeze()
        return cfg


if __name__ == '__main__':
    ImageClassificationTrain()
