import pandas as pd
import requests
from typing import List, Union

from tonic_api.services.models import ModelService
from tonic_api.classes.model import Model
from tonic_api.classes.httpclient import HttpClient


class TrainedModel:
    """Wrapper class for accessing trained models.

    Attributes
    ----------
    id : str
        id of model
    job_id : str
        id of training job
    workspace_id : str
        id of workspace
    model :  Model
        the Tonic Model object
    model_service : ModelService
        service for accessing Tonic Model
    """

    def __init__(
        self, id: str, job_id: str, workspace_id: str, model: Model, client: HttpClient
    ):
        self.id = id
        self.job_id = job_id
        self.workspace_id = workspace_id
        self.model = model
        self.client = client
        self.model_service = ModelService(client)

    def sample(self, num_rows: int=1) -> pd.DataFrame:
        """Generates synthetic samples from trained_model.

        Parameters
        ----------
        num_rows : int, optional
            Number of rows to generate.

        Returns
        -------
        pandas.DataFrame
            A dataframe of synthetic data.
        """
        res = self.model_service.sample(self.id, num_rows)
        return self.__convert_to_df(res)

    def conditional_sample(
        self, conditions: Union[List[dict], pd.DataFrame]
    ) -> pd.DataFrame:
        """Generates synthetic samples from from conditional model, or throws an error
        if the model is not conditional.

        The synthetic samples will be generated based on the specified conditions, with
        one complete sequence of samples for each condition. Note that the sequences
        will be returned in the same order as the conditions, as the conditions will
        be present in the output dataframe.
        
        The conditions parameter can be a list of dictionaries, or a pandas DataFrame. 
        In either case, the values of all condition columns must be specified.

        Parameters
        ----------
        conditions : List[dict] or pd.DataFrame
            List or dataframe of conditions. If a list, each list item should be a 
            dictionary with keys for each condition column and values for the condition. 
            If a dataframe, the extra columns will be dropped and the remaining columns 
            will be used as conditions.

        Returns
        -------
        pandas.DataFrame
            A dataframe of synthetic data.
        """
        if not self.model.has_conditions:
            raise ValueError("Model does not have conditions")

        if isinstance(conditions, pd.DataFrame):
            columns = conditions.columns.tolist()
            for col in columns:
                if col not in self.model.conditions:
                    print("Ignoring column " + col + " not in conditions")
            conditions = conditions[self.model.conditions].to_dict("records")

        try:
            res = self.model_service.conditional_sample(self.id, conditions)
            return self.__convert_to_df(res)
        except requests.exceptions.RequestException as err:
            print('ERROR: {}'.format(err.response.text))

    def sample_source(self, num_rows: int=1):
        """Generates samples from source data.

        Parameters
        ----------
        num_rows : int, optional
            Number of rows to generate.

        Returns
        -------
        pandas.DataFrame
            A dataframe of real data.

        Examples
        --------
        >>> synth_df = model.sample(1000)
        """
        res = self.model_service.sample_source(
            self.workspace_id, self.model.query, num_rows
        )
        columns = res["columns"]
        if len(columns) == 0:
            raise Exception("No data returned from source database")

        n_rows_returned = len(columns[0]["data"])
        converted_res = [{} for _ in range(n_rows_returned)]

        if n_rows_returned < num_rows:
            print(
                "Not enough rows in source destination to sample, limiting to "
                + str(n_rows_returned)
                + " rows."
            )

        for col in columns:
            data = col["data"]
            for idx, val in enumerate(data):
                converted_res[idx][col["columnName"]] = val
        return self.__convert_to_df(converted_res)

    def get_numeric_columns(self) -> List[str]:
        """Returns list of columsn with numeric encodings.
        
        Returns
        -------
        List[str]
        """

        return [
            col
            for (col, encoding) in self.model.encodings.items()
            if encoding == "Numeric"
        ]

    def get_categorical_columns(self) -> List[str]:
        """Returns list of columns with categorical encodings.
        
        Returns
        -------
        List[str]
        """
        return [
            col
            for (col, encoding) in self.model.encodings.items()
            if encoding == "Categorical"
        ]

    def get_condition_columns(self) -> List[str]:
        conditions = self.model.conditions
        if conditions is not None or len(conditions) > 0:
            return conditions
        print("No conditions found")

    def __convert_to_df(self, sample_response):
        schema = self.__get_schema()
        df = pd.DataFrame(sample_response)
        df = self.__conform_df_to_schema(df, schema)
        return df

    def __get_schema(self):
        schema = self.model_service.get_schema(self.workspace_id, self.model.query)
        ordered_schema = self.__convert_schema_to_ordered_col_list(schema)
        return ordered_schema

    def __convert_schema_to_ordered_col_list(self, schema):
        return [
            obj["columnName"]
            for obj in sorted(schema, key=lambda v: v["ordinalPosition"])
        ]

    def __conform_df_to_schema(self, df, schema):
        return df.reindex(schema, axis=1)

    def describe(self):
        """Prints description of trained model."""
        print("Trained Model: [" + self.id + "]")
        print("Job ID: " + self.job_id)
        print("Workspace ID: " + self.workspace_id)
        print("Model: ")
        self.model.describe()
