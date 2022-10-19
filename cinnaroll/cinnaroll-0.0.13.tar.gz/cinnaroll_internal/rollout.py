import time
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


# todo: uncomment or implement in another way (images probably shouldn't be pickled)
def pickle_input_samples(model_input_sample: Any, infer_func_input_sample: Any) -> None:
    # for sample, filename in (model_input_sample, PICKLED_MODEL_INPUT_SAMPLE_FILENAME), (
    #     infer_func_input_sample,
    #     PICKLED_INFER_FUNC_INPUT_SAMPLE_FILENAME,
    # ):
    #     with open(filename, "wb") as handle:
    #         pickle.dump(sample, handle)
    pass


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
    print("Validating config pre-training...")
    pre_training_errors = pre_training_validation.find_config_pre_training_errors(
        config
    )

    if len(pre_training_errors):
        for e in pre_training_errors:
            print(repr(e))
        raise RolloutConfigurationError

    print("Pre-training validation OK! Great!")

    print("Inferring framework...")
    framework = model.infer_framework(config.model_object)
    cinnaroll_model = model.create_model(config.model_object, framework)

    if model.is_trained_in_script(config.train_eval):
        try:
            if cinnaroll_model.should_be_loaded():
                print("Loading saved model...")
                config.model_object = cinnaroll_model.load()
                print("Loaded successfully!")
            else:
                print("Training model...")
                config.train_eval()
                print("Model trained!")
                print("Saving model...")
                cinnaroll_model.save()  # todo: handle model saving error!!!!!!!
                print("Model saved!")

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

    print("Validating config post-training...")

    post_training_errors = post_training_validation.find_config_post_training_errors(
        cinnaroll_model=cinnaroll_model,
        config=config,
    )
    if len(post_training_errors):
        for err in post_training_errors:
            print(repr(err))
        raise RolloutConfigurationError
    print("Post-training validation OK! Great!")

    print("Fetching model metadata...")
    model_metadata = cinnaroll_model.get_metadata()
    print("Fetching environment info...")
    user_environment_info = environment_info.EnvironmentInfo(framework)
    print("Creating model artifact...")
    infer_func_source_code = get_full_infer_func_source_code(config.infer)
    pickle_input_samples(config.model_input_sample, config.infer_func_input_sample)
    print("Sending rollout data to cinnaroll backend...")

    send_rollout_data(
        config=config,
        infer_func_source_code=infer_func_source_code,
        framework=framework,
        user_environment_info=user_environment_info,
        model_metadata=model_metadata,
    )
    
    print("Uploading model and input samples...")
    time.sleep(5)  # todo: delete
    upload_model()
    upload_input_samples()
    print("Success!")
    print("Congratulations! You've configured cinnaroll rollout successfully!")
