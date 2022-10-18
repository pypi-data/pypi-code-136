from autosklearn.experimental.askl2 import AutoSklearn2Classifier
import autosklearn.regression
import sklearn


def get_x_y(dataset):
    y = dataset["label"]
    X = dataset.drop("label", axis=1)
    return X, y


def automl(dataset, type):
    X, y = get_x_y(dataset)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, random_state=42
    )
    if type == "classification":
        automl = AutoSklearn2Classifier(
            time_left_for_this_task=120,
            per_run_time_limit=30,
            ensemble_nbest=5,
            tmp_folder="/tmp/autosklearn_classification_example_tmp",
        )
        automl.fit(X_train, y_train)
        predictions = automl.predict(X_test)
        return {
            "models": automl.show_models(),
            "score": sklearn.metrics.accuracy_score(y_test, predictions),
        }
    elif type == "regression":
        automl = autosklearn.regression.AutoSklearnRegressor(
            time_left_for_this_task=120,
            per_run_time_limit=30,
            ensemble_nbest=5,
            tmp_folder="/tmp/autosklearn_regression_example_tmp",
        )
        automl.fit(X_train, y_train)
        predictions = automl.predict(X_test)
        return {
            "models": automl.show_models(),
            "score": sklearn.metrics.r2_score(y_test, predictions),
        }
