import pickle
from typing import Any, Callable, Dict, List, Tuple

from cinnaroll_internal import (
    environment_info,
    model,
    post_training_validation,
    pre_training_validation,
    rollout_config,
)


class RolloutConfigurationError(Exception):
    ...


class ConfigParameterUndefinedError(Exception):
    ...


PICKLED_MODEL_INPUT_SAMPLE_FILENAME = "model_input_sample.pickle"
PICKLED_INFER_FUNC_INPUT_SAMPLE_FILENAME = "infer_func_input_sample.pickle"


# todo: if dict config is chosen, refactor this to return RolloutConfig and errors
# get stuff, don't transform data but return errors if something besides metrics is missing (key errors and None values)
# try to create RolloutConfig out of what's in dict
# catch type errors and reformat them to make them easier to understand
# return RolloutConfig and errors
def get_config_from_dict(
    config: Dict[str, Any]
) -> Tuple[rollout_config.RolloutConfig, List[Exception]]:
    pass


# get source code of infer_func and everything it needs for serving inferences - imports, variables etc.
# use app.extract.crawler
def get_full_infer_func_source_code(infer_func: Callable[[Any, Any], Any]) -> str:
    pass


def pickle_input_samples(model_input_sample: Any, infer_func_input_sample: Any) -> None:
    for sample, filename in (model_input_sample, PICKLED_MODEL_INPUT_SAMPLE_FILENAME), (
        infer_func_input_sample,
        PICKLED_INFER_FUNC_INPUT_SAMPLE_FILENAME,
    ):
        with open(filename, "wb") as handle:
            pickle.dump(sample, handle)


# create a json containing everything needed besides files and send it to backend
def send_rollout_data(
    *,
    config: rollout_config.RolloutConfig,
    infer_func_source_code: Any,
    framework: str,
    user_environment_info: environment_info.EnvironmentInfo,
    model_metadata: Any,
) -> None:
    pass


def upload_model() -> None:
    pass


def upload_input_samples() -> None:
    pass


def rollout(config: rollout_config.RolloutConfig) -> None:
    pre_training_errors = pre_training_validation.find_config_pre_training_errors(
        config
    )

    if len(pre_training_errors):
        for e in pre_training_errors:
            print(repr(e))
        raise RolloutConfigurationError

    framework = model.infer_framework(config.model_object)
    cinnaroll_model = model.create_model(config.model_object, framework)

    # if there's no training, model should be loaded somewhere in the script
    if model.is_trained_in_script(config.train_eval):
        try:
            if cinnaroll_model.should_be_loaded():
                config.model_object = cinnaroll_model.load()
        except model.ModelLoadingError as e:
            user_input = ""
            while user_input not in ("y", "yes", "n", "no"):
                user_input = input(
                    f"Loading the model failed with the following error: {repr(e)} Train? y/n "
                )
                if user_input in ("y", "yes"):
                    config.train_eval()
                    cinnaroll_model.save()
                elif user_input in ("n", "no"):
                    return
        else:
            config.train_eval()
            cinnaroll_model.save()

    post_training_errors = post_training_validation.find_config_post_training_errors(
        cinnaroll_model=cinnaroll_model,
        config=config,
    )
    if len(post_training_errors):
        for err in post_training_errors:
            print(repr(err))
        raise RolloutConfigurationError

    model_metadata = cinnaroll_model.get_metadata()
    user_environment_info = environment_info.EnvironmentInfo(framework)
    infer_func_source_code = get_full_infer_func_source_code(config.infer)
    pickle_input_samples(config.model_input_sample, config.infer_func_input_sample)

    send_rollout_data(
        config=config,
        infer_func_source_code=infer_func_source_code,
        framework=framework,
        user_environment_info=user_environment_info,
        model_metadata=model_metadata,
    )
    cinnaroll_model.save()
    upload_model()
    upload_input_samples()
    print("Congratulations! You've configured cinnaroll rollout!")
