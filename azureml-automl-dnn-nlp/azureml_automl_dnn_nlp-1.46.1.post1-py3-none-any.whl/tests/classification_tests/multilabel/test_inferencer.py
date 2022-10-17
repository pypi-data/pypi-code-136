from pandas.util.testing import assert_frame_equal
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest
import torch

from azureml.automl.dnn.nlp.classification.common.constants import DatasetLiterals
from azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer import MultilabelInferencer
from azureml.automl.dnn.nlp.classification.io.read.dataloader import get_y_transformer
from azureml.automl.dnn.nlp.common.constants import DataLiterals, SystemSettings
from ...mocks import (
    aml_dataset_mock, aml_label_dataset_mock,
    get_multilabel_labeling_df, MockRun, open_classification_file
)


class TestMultilabelInferencer:
    @pytest.mark.usefixtures('MultilabelDatasetTester')
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.load_model_wrapper")
    @pytest.mark.parametrize('multiple_text_column', [False, True])
    def test_predict(self, load_model_wrapper_mock, MultilabelDatasetTester, multiple_text_column):
        input_df = MultilabelDatasetTester.get_data().copy()
        label_column_name = "labels_col"
        y_transformer = get_y_transformer(input_df, input_df, label_column_name)
        num_label_cols = len(y_transformer.classes_)
        assert num_label_cols == 6
        run = MockRun()
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        inferencer = MultilabelInferencer(run, device)

        columns_to_drop = [label_column_name, DatasetLiterals.DATAPOINT_ID]
        input_df = input_df[input_df.columns.difference(columns_to_drop)]

        mock_model_wrapper = MagicMock()
        mock_model_wrapper.predict_proba.return_value = [[0.38286376, 0.95930564],
                                                         [0.3904482, 0.60089535],
                                                         [0.25657248, 0.7936413],
                                                         [0.94077146, 0.13318592],
                                                         [0.9345981, 0.59357965]] * 10
        expected_label_conf = ['0.38286376,0.95930564',
                               '0.3904482,0.60089535',
                               '0.25657248,0.7936413',
                               '0.94077146,0.13318592',
                               '0.9345981,0.59357965'] * 10

        mock_model_wrapper.dataset_language.return_value = "eng"
        load_model_wrapper_mock.return_value = mock_model_wrapper

        label_list = np.array(['1', '2', 'A', 'a', 'label5', 'label6'])

        predicted_df = inferencer.predict(mock_model_wrapper, y_transformer,
                                          input_df, label_column_name)

        assert len(predicted_df) == 50
        if multiple_text_column:
            assert all(column in ['text', 'text_second', label_column_name,
                                  DataLiterals.LABEL_CONFIDENCE] for column in predicted_df.columns)
            assert predicted_df.shape == (50, 4)
        else:
            assert all(column in ['text', label_column_name,
                                  DataLiterals.LABEL_CONFIDENCE] for column in predicted_df.columns)
            assert predicted_df.shape == (50, 3)
        assert all(item in predicted_df[label_column_name][0] for item in label_list)
        assert all(item in expected_label_conf for item in predicted_df[DataLiterals.LABEL_CONFIDENCE])
        assert sum(predicted_df.columns.values == label_column_name) == 1

    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.save_predicted_results")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.MultilabelInferencer.predict")
    @patch("azureml.core.Dataset.get_by_id")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.load_model_wrapper")
    @pytest.mark.usefixtures('MultilabelDatasetTester')
    @pytest.mark.parametrize('multiple_text_column', [False, True])
    def test_score(
            self,
            load_model_wrapper_mock, get_by_id_mock, predict_mock, save_predicted_results_mock,
            MultilabelDatasetTester
    ):
        label_column_name = "label"
        mock_run = MockRun(
            label_column_name=label_column_name
        )

        mock_model_wrapper = MagicMock()
        mock_model_wrapper.dataset_language.return_value = "eng"
        load_model_wrapper_mock.return_value = mock_model_wrapper

        input_df = MultilabelDatasetTester.get_data().copy()
        mock_aml_dataset = aml_dataset_mock(input_df)
        get_by_id_mock.return_value = mock_aml_dataset

        predicted_df = pd.DataFrame(
            [['A,a,1,2,label5,label6', '0.1,0.2,0.3,0.4,0.5,0.6'] for i in range(input_df.shape[0])],
            columns=[label_column_name, DataLiterals.LABEL_CONFIDENCE]
        )
        predict_mock.return_value = predicted_df

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        inferencer = MultilabelInferencer(mock_run, device)

        output_df = inferencer.score(input_dataset_id="some_dataset_id")

        assert_frame_equal(predicted_df, output_df)
        assert predict_mock.call_count == 1
        assert save_predicted_results_mock.call_count == 1

    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.load_model_wrapper")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer."
           "generate_predictions_output_for_labeling_service")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.MultilabelInferencer.predict")
    @patch("azureml.core.Dataset.get_by_id")
    def test_score_labeling_service(
            self, get_by_id_mock, predict_mock, generate_output_mock, load_model_wrapper_mock
    ):
        label_column_name = "label"
        mock_run = MockRun(
            run_source=SystemSettings.LABELING_RUNSOURCE,
            label_column_name=label_column_name,
            labeling_dataset_type="FileDataset"
        )

        mock_model_wrapper = MagicMock()
        mock_model_wrapper.dataset_language.return_value = "eng"
        load_model_wrapper_mock.return_value = mock_model_wrapper

        mock_aml_dataset = aml_label_dataset_mock('TextClassificationMultiLabel', get_multilabel_labeling_df())
        get_by_id_mock.return_value = mock_aml_dataset

        predicted_df = pd.DataFrame(
            [
                ["label_1,label_2", '0.758,0.323'],
                ["label_1,label_2", '0.831,0.418']
            ] * 30,
            columns=[DataLiterals.LABEL_COLUMN, DataLiterals.LABEL_CONFIDENCE]
        )
        predict_mock.return_value = predicted_df

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        inferencer = MultilabelInferencer(mock_run, device)

        with patch("azureml.automl.dnn.nlp.classification.io.read._labeling_data_helper.open",
                   new=open_classification_file):
            output_df = inferencer.score(input_dataset_id="some_dataset_id")

        assert_frame_equal(predicted_df, output_df)
        assert predict_mock.call_count == 1
        assert generate_output_mock.call_count == 1

    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.load_model_wrapper")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.save_predicted_results")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.MultilabelInferencer.predict")
    @patch("azureml.core.Dataset.get_by_id")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer."
           "is_data_labeling_run_with_file_dataset")
    @pytest.mark.usefixtures('MultilabelDatasetTester')
    @pytest.mark.parametrize('multiple_text_column', [False, True])
    @pytest.mark.parametrize('enable_datapoint_id_output', [True, False])
    def test_score_enable_datapoint_id_output(
            self, is_data_labeling_run_with_file_dataset_mock,
            get_by_id_mock, predict_mock, save_predicted_results_mock, load_model_wrapper_mock,
            MultilabelDatasetTester, enable_datapoint_id_output
    ):
        # Labeling run but tabular dataset input
        is_data_labeling_run_with_file_dataset_mock.return_value = False

        label_column_name = "labels_col"
        mock_run = MockRun(
            run_source=SystemSettings.LABELING_RUNSOURCE,
            label_column_name=label_column_name,
            labeling_dataset_type="TabularDataset"
        )

        mock_model_wrapper = MagicMock()
        mock_model_wrapper.dataset_language.return_value = "eng"
        load_model_wrapper_mock.return_value = mock_model_wrapper

        input_df = MultilabelDatasetTester.get_data().copy()
        input_df[DatasetLiterals.DATAPOINT_ID] = [f"id_{i}" for i in range(input_df.shape[0])]
        mock_aml_dataset = aml_dataset_mock(input_df)
        get_by_id_mock.return_value = mock_aml_dataset

        predicted_df = pd.DataFrame(
            [['A,a,1,2,label5,label6', '0.1,0.2,0.3,0.4,0.5,0.6'] for i in range(input_df.shape[0])],
            columns=[label_column_name, DataLiterals.LABEL_CONFIDENCE]
        )
        predict_mock.return_value = predicted_df

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        inferencer = MultilabelInferencer(mock_run, device)

        output_df = inferencer.score(input_dataset_id="some_dataset_id",
                                     enable_datapoint_id_output=enable_datapoint_id_output)

        if enable_datapoint_id_output:
            assert sorted(output_df.columns) == sorted([DatasetLiterals.DATAPOINT_ID,
                                                        label_column_name, "label_confidence"])
            assert output_df[DatasetLiterals.DATAPOINT_ID].equals(input_df[DatasetLiterals.DATAPOINT_ID])
        else:
            assert sorted(output_df.columns) == sorted([label_column_name, "label_confidence"])
        assert predict_mock.call_count == 1
        assert save_predicted_results_mock.call_count == 1

    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.load_model_wrapper")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.save_predicted_results")
    @patch("azureml.automl.dnn.nlp.classification.inference.multilabel_inferencer.MultilabelInferencer.predict")
    @patch("azureml.data.abstract_dataset.AbstractDataset._load")
    @pytest.mark.usefixtures('MultilabelDatasetTester')
    @pytest.mark.parametrize('multiple_text_column', [False])
    def test_score_mltable_uri(
            self,
            load_dataset_mock, predict_mock, save_predicted_results_mock, load_model_wrapper_mock,
            MultilabelDatasetTester
    ):
        label_column_name = "label"
        mock_run = MockRun(
            label_column_name=label_column_name
        )

        mock_model_wrapper = MagicMock()
        mock_model_wrapper.dataset_language.return_value = "eng"
        load_model_wrapper_mock.return_value = mock_model_wrapper

        input_df = MultilabelDatasetTester.get_data().copy()
        mock_aml_dataset = aml_dataset_mock(input_df)
        load_dataset_mock.return_value = mock_aml_dataset

        predicted_df = pd.DataFrame(
            [['A,a,1,2,label5,label6', '0.1,0.2,0.3,0.4,0.5,0.6'] for i in range(input_df.shape[0])],
            columns=[label_column_name, DataLiterals.LABEL_CONFIDENCE]
        )
        predict_mock.return_value = predicted_df

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        inferencer = MultilabelInferencer(mock_run, device)

        output_df = inferencer.score(input_mltable_uri="mock_mltable_uri")

        assert_frame_equal(predicted_df, output_df)
        assert predict_mock.call_count == 1
        assert save_predicted_results_mock.call_count == 1
