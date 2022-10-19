import sys
from .. import config
from . import initial_sherlock_necessary

import numpy as np
import pandas as pd

try:
    from sherlock.deploy.model import SherlockModel
    from sklearn.preprocessing import LabelEncoder
except ImportError as e:
    print(
'''
to install sherlock you can run: 'pip install -e git+https://github.com/mitmedialab/sherlock-project.git#egg=sherlock'
or 
>> from sherlock_assistance import sherlock_installing
>> sherlock_installing()
**if you run in IPython Notebook restart kernel to re-import after install the package**
''')
    sys.exit(e)

initial_sherlock_necessary()

def categorize_features() -> dict:
    """Get feature identifiers per feature set, to map features to feature sets.

    Returns
    -------
    feature_cols_dict
        Dictionary with lists of feature identifiers per feature set.
    """
    feature_cols_dict = {}
    for feature_set in ["char", "word", "par", "rest"]:
        feature_cols_dict[feature_set] = pd.read_csv(
            f"{config.__statics__}/feature_column_identifiers/{feature_set}_col.tsv",
            sep="\t",
            index_col=0,
            header=None,
            squeeze=True,
        ).to_list()
    return feature_cols_dict

def _proba_to_classes(y_pred, model_id: str = "sherlock") -> np.array:
    """Get predicted semantic types from prediction vectors.

    Parameters
    ----------
    y_pred
        Nested vector with for each sample a vector of likelihoods per semantic type.
    model_id
        Identifier of model to use.

    Returns
    -------
    y_pred
        Predicted semantic labels.
    """
    y_pred_int = np.argmax(y_pred, axis=1)
    encoder = LabelEncoder()
    encoder.classes_ = np.load(
        f"{config.__statics__}/model_files/classes_{model_id}.npy", allow_pickle=True
    )

    y_pred = encoder.inverse_transform(y_pred_int)

    return y_pred

class SherlockSemanticClassifier(SherlockModel):

    def __init__(self,
            model_files_directory = f"{config.__statics__}/model_files/",
            lamb    = 0.0001,
            do      = 0.35,
            lr      = 0.0001
        ):
        self.lamb = lamb
        self.do = do
        self.lr = lr

        self.model_files_directory = model_files_directory

    def predict(self, X: pd.DataFrame, model_id: str = "sherlock") -> np.array:
        """Use sherlock model to generate predictions for X.

        Parameters
        ----------
        X
            Featurized dataframe to generate predictions for.
        model_id
            ID of the model used for generating predictions.

        Returns
        -------
        Array with predictions for X.
        """
        y_pred = self.predict_proba(X, model_id)
        y_pred_classes = _proba_to_classes(y_pred, model_id)

        return y_pred_classes

    def predict_proba(self, X: pd.DataFrame, model_id: str = "sherlock") -> np.array:
        """Use sherlock model to generate predictions for X.

        Parameters
        ----------
        X
            Featurized data set to generate predictions for.
        model_id
            Identifier of a trained model to use for generating predictions.

        Returns
        -------
        Array with predictions for X.
        """
        feature_cols_dict = categorize_features()

        y_pred = self.model.predict(
            [
                X[feature_cols_dict["char"]].values,
                X[feature_cols_dict["word"]].values,
                X[feature_cols_dict["par"]].values,
                X[feature_cols_dict["rest"]].values,
            ]
        )

        return y_pred