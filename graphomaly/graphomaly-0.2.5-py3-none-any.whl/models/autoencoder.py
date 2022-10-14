# Copyright (c) 2021 Alexandra Bodirlau <alexandra.bodirlau@tremend.com>, Tremend Software Consulting
# Copyright (c) 2021 Stefania Budulan <stefania.budulan@tremend.com>, Tremend Software Consulting
# Copyright (c) 2022 Paul Irofti <paul@irofti.net>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import activations, layers
from tensorflow.keras.regularizers import L2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau


@tf.keras.utils.register_keras_serializable()
class Autoencoder(tf.keras.Model):
    """Autoencoder model introduced by Aggarwal C. [1]_

    Parameters
    ----------
    encoder_neurons : list
        The number of neurons per encoder layers.

    decoder_neurons : list
        The number of neurons per decoder layers.

    activation_function : str or callable, default='tanh'
        The activation function for all layers.
        See `Keras doc <https://keras.io/api/layers/activations/>`_.

    l2_regularizer : float in (0., 1), default=0.1
        The regularization factor for L2 regularizer for all layers.

    dropout : float in (0., 1), default=0.2
        Dropout rate for all hidden layers.

    threshold : float, default=None
        The threshold used for anomalies selection. If None, the
        contamination is used to compute the threshold.

    contamination : float, default=0.1
        The contamination rate used for computing the reconstruction error
        threshold. Used if threshold is not set.

    Attributes
    ----------
    reconstruction_errors_ : array-like of shape (n_samples,)
        The raw outlier scores for the training data. The anomalies have
        a larger error score.

    history_ : Keras Object
        The training history of the model.

    labels_ : list of int (0 or 1)
        The binary labels for the training data. 0 means inliers and 1 means
        outliers.

    threshold_ : float
        The threshold for the raw outliers scores.

    References
    ----------
    .. [1] Aggarwal C. (2015) Outlier Analysis. In: Data Mining. Springer,
        Cham. https://doi.org/10.1007/978-3-319-14142-8_8
    """

    def __init__(
        self,
        encoder_neurons=None,
        decoder_neurons=None,
        activation_function="tanh",
        l2_regularizer=0.1,
        dropout=0.2,
        threshold=None,
        contamination=0.1,
        optimizer=None,
        loss=None,
        epochs=None,
        batch_size=None,
        shuffle=None,
        validation_size=None,
    ):
        super(Autoencoder, self).__init__()

        self.encoder_neurons = encoder_neurons
        self.decoder_neurons = decoder_neurons
        self.activation_function = activation_function
        self.l2_regularizer = l2_regularizer
        self.dropout = dropout
        self.contamination = contamination
        self.threshold = threshold
        self.classes = 2
        self.reconstruction_errors_ = None
        self.history_ = None
        self.labels_ = None

        self.optimizer = optimizer
        self.loss = loss
        self.epochs = epochs
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.validation_size = validation_size

        self._check_parameters()
        self._build_model()

    # See here: https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable
    # "To be serialized and deserialized, classes must implement the get_config() method."
    def get_config(self):
        return {"encoder_neurons": self.encoder_neurons,
                "decoder_neurons": self.decoder_neurons,
                "activation_function": self.activation_function,
                "l2_regularizer": self.l2_regularizer,
                "dropout": self.dropout,
                "threshold": self.threshold,
                "contamination": self.contamination,
                "classes": self.classes,
                "reconstruction_errors_": self.reconstruction_errors_,
                "history_": self.history_,
                "labels_": self.labels_,
                "optimizer": self.optimizer,
                "loss": self.loss,
                "epochs": self.epochs,
                "batch_size": self.batch_size,
                "shuffle": self.shuffle,
                "validation_size": self.validation_size
        }

    def _build_model(self):
        encoder_layers = []
        for neurons in self.encoder_neurons:
            linear_layer = layers.Dense(
                neurons,
                activation=self.activation_function,
                activity_regularizer=L2(self.l2_regularizer),
            )
            dropout_layer = layers.Dropout(self.dropout)

            encoder_layers.append(linear_layer)
            encoder_layers.append(dropout_layer)

        decoder_layers = []
        for ilayer, neurons in enumerate(self.decoder_neurons):

            # The last layer should have no activation function
            activation = self.activation_function
            if ilayer == len(self.decoder_neurons)-1:
                activation = 'linear'

            linear_layer = layers.Dense(
                neurons,
                activation=activation,
                activity_regularizer=L2(self.l2_regularizer),
            )
            dropout_layer = layers.Dropout(self.dropout)

            decoder_layers.append(linear_layer)
            decoder_layers.append(dropout_layer)

        self.encoder = tf.keras.Sequential(encoder_layers, name="encoder")
        self.decoder = tf.keras.Sequential(decoder_layers[:-1], name="decoder")

    def call(self, inputs):
        if inputs.shape[1] != self.decoder_neurons[-1]:
            raise ValueError(
                "Expected the number of features to be equal to "
                "the number of neurons on the last decoder layer. "
                f"But found: {inputs.shape[1]} features and "
                f"{self.decoder_neurons[-1]} neurons."
            )

        encoded = self.encoder(inputs)
        decoded = self.decoder(encoded)

        return decoded

    def summary(self):
        """Print Autoencoder architecture on components."""
        print(self.encoder.summary())
        print(self.decoder.summary())

    def predict_reconstruction_error(self, X):
        """Predict the reconstruction errors for some samples.
        The anomalies have a larger error score.

        This does not modify the object. Use for prediction, not fitting.

        Parameters
        ----------
        X : array-like of shape (num_samples, num_features)
            The samples for which to compute the scores.

        Returns
        -------
        ndarray of shape (num_samples, )
            The reconstruction error scores.
        """
        preds = super().predict(X)
        return Autoencoder._compute_scores(X, preds)

    def predict_proba(self, X=None, method="linear", thresh=None):
        """Compute a distribution probability on the reconstuction errors
        predicted for the samples passed as parameter. The scores as
        normalized using a scaler fitted on the train scores, so the method
        predict_decision_scores() must be called after training the model
        in order to be able to compute the probabilities.

        This does not modify the object. Use for prediction, not fitting.

        If X is not None, the errors are computed for the data in X
        If X is None, assume the erorrs are already available in self.reconstruction_errors_

        Parameters
        ----------
        X : array-like of shape (num_samples, num_features)
            The samples for which to compute the probabilities.

        method : {'linear', 'hard', 'quantile'}, default='linear'
            The method used for score normalization. 
            'linear': scale scores to [0, 1] range
            'hard': hard thresholding with a given threshold `thresh`, return binary scores. If `thresh` is None, use self.threshold instead.
            'quantile': hard thresholding using the given quantile in `thresh`, 
                        e.g. thresh=0.1 assigns 0 to the smallest 10% errors, and 1 to the largest 90% errors.

        Returns
        -------
        ndarray of shape (num_samples, )
            The probabilities for each class (normal prob on dimension 0,
            anomaly prob on dimension 1).
        """

        # If X is None, we process the error values stored in self.reconstruction_errors_
        if X is None and self.reconstruction_errors_ is None:
            raise Exception(
                "Reconstruction errors on train set are not available."
            )

        rec_errors = self.predict_reconstruction_error(X) if X is not None else self.reconstruction_errors_

        probs = np.zeros([rec_errors.shape[0], self.classes])

        if method == "linear":
            scaler = MinMaxScaler()
            probs[:, 1] = scaler.fit_transform(rec_errors.reshape(-1, 1)).squeeze()
            probs[:, 0] = 1 - probs[:, 1]

        elif method == "hard" and (thresh is not None or self.threshold is not None):
            thresh_local = thresh if thresh is not None else self.threshold   # given threshold, or fitted one
            probs[:, 1] = (rec_errors > thresh_local).astype("int")

        elif method == "quantile" and thresh is not None:
            q_thresh = np.quantile(rec_errors, thresh)
            probs[:, 1] = (rec_errors > q_thresh).astype("int")

        else:
            raise ValueError(
                f"method={method}, thresh={thresh} is not a valid combination for probability conversion."
            )

        return probs

    def set_params(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def get_params(self, deep=True):
        return {
            "encoder_neurons": self.encoder_neurons,
            "decoder_neurons": self.decoder_neurons,
            "activation_function": self.activation_function,
            "l2_regularizer": self.l2_regularizer,
            "dropout": self.dropout,
            "contamination": self.contamination,
            "threshold": self.threshold,
            "optimizer": self.optimizer,
            "loss": self.loss,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "shuffle": self.shuffle,
            "validation_size": self.validation_size,
            #reconstruction_errors_?
            #history_?
            #labels_?
        }

    def fit(self, X, y=None, **kwargs):
        self.set_params(**kwargs)

        self.compile(optimizer=self.optimizer, loss=self.loss)

        # Monitor validation loss, stop after 50 epochs not improving, get best model
        es = EarlyStopping(monitor=self.monitor, patience=self.patience, restore_best_weights=True)

        # Reduce learning-rate on plateau
        reduce_lr = ReduceLROnPlateau(monitor=self.monitor, factor=self.learning_rate_reduce_factor, 
                                        patience=10, min_lr=self.learning_rate_min)

        self.history_ = (
            super()
            .fit(
                X,
                X,
                epochs=self.epochs,
                batch_size=self.batch_size,
                validation_split=self.validation_size,
                shuffle=self.shuffle,
                verbose=self.verbose,
                callbacks=[es, reduce_lr]
            )
            .history
        )

        # Fit the threshold, based on the reconstruction errors on the training set
        self.reconstruction_errors_ = self.predict_reconstruction_error(X)
        if self.threshold is None:
            self.threshold = np.quantile(self.reconstruction_errors_, 1 - self.contamination)

        # Compute the labels on the training set
        self.labels_ = self.predict_proba(method='hard', thresh=self.threshold)[:,1]

        return self

    def predict(self, X):
        """Predict binary labels for the samples passed as parameter.

        This does not modify the object. Use for prediction, not fitting.

        Parameters
        ----------
        X : array-like of shape (num_samples, num_features)
            The samples for which to compute the probabilities.

        Returns
        -------
        ndarray of shape (num_samples, )
            The predicted labels for all input.
        """

        pred_score = self.predict_reconstruction_error(X)
        labels = (pred_score > self.threshold).astype("int")
        return labels

    def fit_predict(self, X, y=None):
        #return self.fit(X, y).predict(X)
        return self.fit(X, y).labels_

    def _check_parameters(self):
        if not isinstance(self.encoder_neurons, list):
            raise TypeError(
                "Expected encoder_neurons to have type list, but "
                f"received {type(self.encoder_neurons)}"
            )

        if not isinstance(self.decoder_neurons, list):
            raise TypeError(
                "Expected decoder_neurons to have type list, but "
                f"received {type(self.encoder_neurons)}"
            )

        if not all(map(lambda x: isinstance(x, int), self.encoder_neurons)):
            raise TypeError("Not all elements from encoder_neurons have int " "type")

        if not all(map(lambda x: isinstance(x, int), self.decoder_neurons)):
            raise TypeError("Not all elements from decoder_neurons have int " "type")

        # Check regularizer type and value
        if not isinstance(self.l2_regularizer, float):
            raise TypeError(
                "Expected l2_regularizer to have type float, but "
                f"received {type(self.l2_regularizer)}"
            )

        if self.l2_regularizer < 0.0 or self.l2_regularizer > 1.0:
            raise ValueError(
                "Expected l2_regularizer to have a value in (0.0,"
                f"1.0) range, but received {self.l2_regularizer}"
            )

        # Check activation_function value and type
        if isinstance(self.activation_function, str):
            try:
                activations.deserialize(str(self.activation_function))
            except ValueError:
                raise ValueError(
                    "activation_function value is not supported. "
                    "Please check: https://keras.io/api/layers/activations/"
                    " for available values."
                )

        elif not isinstance(self.activation_function, callable):
            raise TypeError(
                "Expected activation_function to be str or "
                "callable. Please check: "
                "https://keras.io/api/layers/activations/ for "
                "available values."
            )

        if self.contamination is None and self.threshold is None:
            raise TypeError(
                "Expected 'contamination' or 'threshold' to "
                "be float, but received None."
            )

    @staticmethod
    def _compute_scores(X, Y):
        return np.sqrt(np.sum(np.square(Y - X), axis=1))
